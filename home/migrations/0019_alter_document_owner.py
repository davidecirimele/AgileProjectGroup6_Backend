# Generated by Django 4.1.4 on 2023-01-03 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0018_alter_student_dob"),
    ]

    operations = [
        migrations.AlterField(
            model_name="document",
            name="owner",
            field=models.CharField(max_length=100),
        ),
    ]
