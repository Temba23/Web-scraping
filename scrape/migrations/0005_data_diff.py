# Generated by Django 4.2.7 on 2023-11-05 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrape', '0004_alter_data_ltp'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='diff',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]