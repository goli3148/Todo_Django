# Generated by Django 4.1.7 on 2023-03-06 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50, verbose_name='subject')),
                ('extra', models.TextField(max_length=500, verbose_name='extra')),
                ('date_pub', models.DateField(auto_now_add=True, verbose_name='date published')),
                ('date_upd', models.DateField(auto_now=True, verbose_name='date updated')),
            ],
        ),
    ]