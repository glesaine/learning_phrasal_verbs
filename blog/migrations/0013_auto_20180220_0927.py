# Generated by Django 2.0.2 on 2018-02-20 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_errors'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Errors',
            new_name='Error',
        ),
    ]
