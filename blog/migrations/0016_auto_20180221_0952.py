# Generated by Django 2.0.2 on 2018-02-21 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20180220_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verb',
            name='example',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='verb',
            name='meaning',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='verb',
            name='phrasal_verb',
            field=models.CharField(max_length=100),
        ),
    ]
