# Generated by Django 3.0.2 on 2020-02-02 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='slug',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]
