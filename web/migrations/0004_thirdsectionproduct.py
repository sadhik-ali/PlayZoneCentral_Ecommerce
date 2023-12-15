# Generated by Django 4.2.7 on 2023-11-11 17:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0003_alter_firstsectionproduct_productprice_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ThirdSectionProduct",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ProductImage", models.ImageField(upload_to="media")),
                ("ProductName", models.CharField(max_length=100)),
                ("ProductPrice", models.IntegerField()),
            ],
        ),
    ]
