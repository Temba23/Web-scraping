# Generated by Django 4.2.7 on 2023-11-01 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10)),
                ('ltp', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
