# Generated by Django 3.0.2 on 2020-02-02 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-creation_date']},
        ),
    ]