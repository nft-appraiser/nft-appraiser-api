# Generated by Django 4.0 on 2021-12-09 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskA', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taska_table',
            name='img',
        ),
    ]
