# Generated by Django 4.1.3 on 2022-11-26 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0001_initial"),
        ("documents", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SecondaryEducation",
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
                ("year_of_enrollment", models.DateField()),
                ("year_of_graduation", models.DateField()),
                ("country", models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name="document",
            name="date_of_expiration",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="document",
            name="date_of_issue",
            field=models.DateField(),
        ),
        migrations.CreateModel(
            name="Student",
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
                (
                    "document_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="documents.document",
                    ),
                ),
                (
                    "secondary_education",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="documents.secondaryeducation",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="secondaryeducation",
            name="student_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="documents.document"
            ),
        ),
        migrations.CreateModel(
            name="MastersDegree",
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
                ("university_nation", models.CharField(max_length=15)),
                ("year_of_enrollment", models.DateField()),
                ("year_of_graduation", models.DateField()),
                ("masters_grade", models.CharField(max_length=10)),
                ("minimum_masters_grade", models.IntegerField()),
                ("maximum_masters_grade", models.IntegerField()),
                (
                    "discipline",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="courses.discipline",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="documents.student",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Doctorate",
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
                ("university_nation", models.CharField(max_length=15)),
                ("year_PhD_started", models.DateField()),
                ("year_PhD_ended", models.DateField()),
                ("doctorate_grade", models.CharField(max_length=10)),
                ("minimum_doctorate_mark", models.IntegerField()),
                ("maximum_doctorate_mark", models.IntegerField()),
                (
                    "discipline",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="courses.discipline",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="documents.student",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BachelorsDegree",
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
                ("university_nation", models.CharField(max_length=15)),
                ("year_of_enrollment", models.DateField()),
                ("year_of_graduation", models.DateField()),
                ("bachelors_grade", models.CharField(max_length=10)),
                ("minimum_bachelor_mark", models.IntegerField()),
                ("maximum_bachelor_mark", models.IntegerField()),
                (
                    "discipline",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="courses.discipline",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="documents.student",
                    ),
                ),
            ],
        ),
    ]
