# Generated by Django 2.0.2 on 2018-02-21 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_datereport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datereport',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='datereport',
            name='success_ratio',
            field=models.FloatField(default=0),
        ),
    ]
