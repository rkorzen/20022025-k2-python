# Generated by Django 5.1.7 on 2025-03-07 13:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=255)),
                ("author", models.CharField(max_length=255)),
                (
                    "year",
                    models.IntegerField(
                        validators=[django.core.validators.MaxValueValidator(2025)]
                    ),
                ),
                ("isbn", models.CharField(blank=True, max_length=255)),
                ("genre", models.CharField(blank=True, max_length=255)),
                ("available", models.BooleanField(default=True)),
                ("added_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("last_borrowed_on", models.DateTimeField(blank=True, null=True)),
                ("last_return_on", models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
