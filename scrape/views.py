from django.shortcuts import render
from .models import Data
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse

def data_input(request):
    # Fetch the webpage
    req = requests.get("https://www.sharesansar.com/today-share-price", verify=False)
    soup = BeautifulSoup(req.content, "html.parser")

    # Find the relevant data
    symbol = soup.find('th', class_="sorting")
    table = soup.find('table', id="headFixed")

    if table:
        # Iterate through table rows to extract data
        rows = table.find_all('tr')[1:]  # Skip the header row
        for row in rows:
            columns = row.find_all('td')
            if len(columns) >= 14:  # Ensure the index is within bounds
                symbol = columns[1].text.strip()
                ltp_str = columns[6].text.strip().replace(',', '')
                diff = columns[12].text.strip()
                print(diff)
                try:
                    ltp = float(ltp_str)
                except ValueError:
                    # Handle cases where ltp_str is not a valid float
                    ltp = 0.0  # You can set a default value or handle the error differently

                # Create or update a Data instance with the extracted data
                data_obj, created = Data.objects.get_or_create(symbol=symbol)
                data_obj.ltp = ltp
                data_obj.diff = diff
                data_obj.save()

    return HttpResponse("Data Retrieved and Saved Successfully.") 

def stock_data_view(request):
    stock_data = Data.objects.all()  # Fetch all stock data
    context = {
        'stock_data': stock_data
    }
    return render(request, 'stock_data.html', context)
