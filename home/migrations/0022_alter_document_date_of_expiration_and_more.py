# Generated by Django 4.1.4 on 2023-01-04 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0021_alter_document_date_of_expiration_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="document",
            name="date_of_expiration",
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name="document",
            name="date_of_issue",
            field=models.CharField(max_length=4),
        ),
    ]
