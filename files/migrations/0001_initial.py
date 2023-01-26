# Generated by Django 4.1.5 on 2023-01-26 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Archive",
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
                ("type", models.CharField(max_length=150)),
                ("date", models.CharField(max_length=150)),
                ("value", models.CharField(max_length=150)),
                ("cpf", models.CharField(max_length=150)),
                ("card", models.CharField(max_length=150)),
                ("hour", models.CharField(max_length=150)),
                ("store_owner", models.CharField(max_length=150)),
                ("store_name", models.CharField(max_length=150)),
            ],
        ),
    ]