# Generated by Django 4.0.2 on 2022-03-03 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='desciption',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]