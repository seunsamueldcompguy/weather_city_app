# Generated by Django 3.0.2 on 2020-07-02 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['-city_name'], 'verbose_name_plural': 'cities'},
        ),
    ]
