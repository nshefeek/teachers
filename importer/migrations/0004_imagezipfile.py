# Generated by Django 3.1.7 on 2021-04-01 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importer', '0003_auto_20210401_1600'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageZipFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.FileField(upload_to='images')),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]