# Generated by Django 2.0.2 on 2018-02-21 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20180221_0952'),
    ]

    operations = [
        migrations.CreateModel(
            name='DateReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('success_ratio', models.IntegerField(default=0)),
                ('date', models.CharField(max_length=100)),
            ],
        ),
    ]
