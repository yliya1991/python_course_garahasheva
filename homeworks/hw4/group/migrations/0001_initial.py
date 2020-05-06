# Generated by Django 2.2.12 on 2020-05-06 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_code', models.PositiveIntegerField()),
                ('group_number', models.PositiveIntegerField()),
                ('form_of_training', models.CharField(max_length=64)),
                ('training_completed', models.BooleanField()),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
            ],
        ),
    ]
