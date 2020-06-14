# Generated by Django 3.0.5 on 2020-06-14 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_pk', models.IntegerField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=500)),
                ('nickname', models.CharField(blank=True, max_length=200)),
                ('point', models.IntegerField(default=0)),
                ('like', models.CharField(blank=True, max_length=200)),
                ('phone', models.CharField(blank=True, max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
