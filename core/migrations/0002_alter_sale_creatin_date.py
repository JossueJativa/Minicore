# Generated by Django 5.0.4 on 2024-04-13 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='creatin_date',
            field=models.DateTimeField(),
        ),
    ]
