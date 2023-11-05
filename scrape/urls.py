from django.urls import path
from . import views


urlpatterns = [

    path('stock-data/', views.stock_data_view, name='stock_data'),
    path('data/', views.data_input, name='stock_data'),

]