# Generated by Django 2.1.5 on 2019-02-11 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predict_site', '0002_auto_20190211_1529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='lesson_hours',
        ),
    ]
