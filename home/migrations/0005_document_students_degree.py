# Generated by Django 4.1.3 on 2022-12-17 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_delete_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=15, unique=True)),
                ('type', models.CharField(max_length=15)),
                ('country_of_issue', models.CharField(max_length=30)),
                ('date_of_issue', models.DateField()),
                ('date_of_expiration', models.DateField()),
                ('authority_issuing_the_document', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_selected', models.CharField(default='BachelorsDegree', max_length=20)),
                ('document_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.document', to_field='id_number')),
            ],
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_degree', models.CharField(max_length=15)),
                ('university_nation', models.CharField(max_length=15)),
                ('year_of_enrollment', models.DateField()),
                ('year_of_graduation', models.DateField()),
                ('discipline', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.discipline')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.document', to_field='id_number')),
            ],
        ),
    ]