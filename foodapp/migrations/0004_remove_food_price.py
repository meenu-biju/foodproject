# Generated by Django 3.2.8 on 2021-10-19 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0003_alter_food_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='price',
        ),
    ]
