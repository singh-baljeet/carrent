# Generated by Django 2.1.1 on 2018-09-22 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('msi', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1000)),
                ('price', models.CharField(max_length=50)),
                ('capacity', models.CharField(max_length=50)),
                ('aircondition', models.CharField(max_length=50)),
                ('transmission', models.CharField(max_length=50)),
            ],
        ),
    ]
