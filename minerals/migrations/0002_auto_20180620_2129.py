# Generated by Django 2.0.6 on 2018-06-20 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minerals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mineral',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
