# Generated by Django 3.2.3 on 2021-05-31 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_quote_sum_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='sum_rating',
            field=models.IntegerField(default=0),
        ),
    ]