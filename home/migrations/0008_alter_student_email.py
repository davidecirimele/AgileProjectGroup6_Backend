# Generated by Django 4.1.4 on 2022-12-30 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0007_alter_student_email_alter_student_phone_no"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="email",
            field=models.EmailField(
                max_length=254, unique=True, verbose_name="email address"
            ),
        ),
    ]
