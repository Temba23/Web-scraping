# Generated by Django 4.2.7 on 2023-11-04 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrape', '0003_alter_data_ltp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='ltp',
            field=models.FloatField(null=True),
        ),
    ]
