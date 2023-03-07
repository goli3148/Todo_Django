# Generated by Django 4.1.7 on 2023-03-06 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='priority',
            field=models.CharField(choices=[('H', 'highPriority'), ('M', 'meduimPriority'), ('L', 'lowPriority')], default='M', max_length=1),
        ),
    ]
