# Generated by Django 4.1.2 on 2025-03-16 13:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0005_product_date_add_alter_tip_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_add',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 16, 18, 57, 50, 829462)),
        ),
    ]
