# Generated by Django 3.1.7 on 2021-03-30 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csvfile',
            name='by',
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='file_name',
            field=models.FileField(upload_to='static/csvs'),
        ),
    ]