# Generated by Django 4.1.4 on 2023-01-04 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0024_alter_degree_student_id_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="degree",
            old_name="student_id",
            new_name="owner",
        ),
    ]
