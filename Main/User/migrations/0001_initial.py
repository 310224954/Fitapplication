# Generated by Django 3.0.2 on 2020-01-30 09:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Food', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TimeField(auto_now_add=True)),
                ('diet_quantity', models.IntegerField(default=100)),
                ('unique_number', models.CharField(max_length=10)),
                ('prod', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Food.Products')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pictures')),
                ('username', models.CharField(max_length=50)),
                ('diet_type', models.CharField(choices=[('1', 'Vegan'), ('2', 'Vegeterian'), ('3', 'Paleo'), ('4', 'Keto'), ('5', 'None')], default='5', max_length=5)),
                ('calories_limit', models.IntegerField(blank=True, default=2500, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Diet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TimeField(auto_now=True)),
                ('diet_prod', models.ManyToManyField(to='User.UserProd')),
                ('profile_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='User.Profile')),
            ],
        ),
    ]