# Generated by Django 5.1.4 on 2025-01-11 07:10

import uuid

from django.db import migrations, models

import common.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "description",
                    models.CharField(max_length=100, verbose_name="Description"),
                ),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=8,
                        validators=[common.validators.validate_not_zero],
                        verbose_name="Amount",
                    ),
                ),
                ("date", models.DateTimeField(verbose_name="Date")),
            ],
            options={
                "verbose_name": "Transaction",
            },
        ),
    ]
