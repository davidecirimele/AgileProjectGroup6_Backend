# Generated by Django 4.1.4 on 2022-12-29 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_alter_student_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
