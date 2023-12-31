# Generated by Django 4.2.7 on 2023-11-14 01:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0014_category_product_delete_book_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product_category",
                to="web.category",
                verbose_name="Product Category",
            ),
        ),
    ]
