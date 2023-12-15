# Generated by Django 4.2.7 on 2023-11-13 05:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0010_rename_gamecart_gamecartsection"),
    ]

    operations = [
        migrations.CreateModel(
            name="gamecartsectiontwo",
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
                ("image", models.ImageField(upload_to="media")),
                ("name", models.CharField(max_length=50)),
                ("price", models.IntegerField()),
            ],
        ),
    ]
