# Generated by Django 2.2.2 on 2019-06-10 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='category',
        ),
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
    ]
