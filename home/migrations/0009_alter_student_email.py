# Generated by Django 4.1.4 on 2023-01-02 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0008_alter_student_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="email",
            field=models.EmailField(max_length=256, unique=True),
        ),
    ]
