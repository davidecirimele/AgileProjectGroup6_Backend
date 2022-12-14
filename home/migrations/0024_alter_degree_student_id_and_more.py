# Generated by Django 4.1.4 on 2023-01-04 16:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0023_alter_document_date_of_expiration_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="degree",
            name="student_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="degree",
            name="year_of_enrollment",
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name="degree",
            name="year_of_graduation",
            field=models.CharField(max_length=4),
        ),
    ]
