# Generated by Django 3.2.8 on 2021-10-18 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('phone', models.IntegerField()),
                ('hotel', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
                ('offer', models.IntegerField()),
                ('payment', models.CharField(max_length=250)),
            ],
        ),
    ]
