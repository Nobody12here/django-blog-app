# Generated by Django 4.1.10 on 2023-07-08 15:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='publish',
            field=models.DateTimeField(verbose_name=django.utils.timezone.now),
        ),
    ]
