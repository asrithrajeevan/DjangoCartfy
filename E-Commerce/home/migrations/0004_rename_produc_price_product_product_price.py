# Generated by Django 4.2.6 on 2023-10-30 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_alter_product_produc_price"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="produc_price",
            new_name="product_price",
        ),
    ]