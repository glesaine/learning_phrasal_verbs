# Generated by Django 2.0.2 on 2018-02-16 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180216_1223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proposition',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('proposition', models.CharField(default='', max_length=100)),
            ],
            options={
                'verbose_name': 'propo',
            },
        ),
    ]
