# Generated by Django 3.0.2 on 2020-01-30 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('protein', models.FloatField()),
                ('carbohydrates', models.FloatField()),
                ('fat', models.FloatField()),
                ('description', models.TextField(blank=True)),
                ('quantity', models.IntegerField(blank=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=100)),
                ('date', models.TimeField(auto_now_add=True)),
                ('food_type', models.CharField(choices=[('1', 'Meat'), ('2', 'Fruit'), ('3', 'Vegetable'), ('4', 'SeaFood'), ('5', 'Nuts'), ('6', 'Grains'), ('7', 'Diary')], max_length=6)),
                ('slug', models.CharField(blank=True, max_length=20, null=True, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ingredient', models.ManyToManyField(to='Food.Products')),
            ],
        ),
    ]
