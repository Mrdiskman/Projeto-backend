# Generated by Django 4.1.5 on 2023-01-26 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("files", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="archive",
            name="value",
            field=models.IntegerField(),
        ),
    ]
