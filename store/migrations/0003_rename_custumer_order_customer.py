# Generated by Django 4.0.2 on 2022-03-04 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_costumer_order_custumer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='custumer',
            new_name='customer',
        ),
    ]