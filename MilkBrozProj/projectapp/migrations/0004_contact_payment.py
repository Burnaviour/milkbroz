# Generated by Django 4.0.5 on 2022-07-04 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0003_rename_number_contact_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='payment',
            field=models.TextField(default='none'),
        ),
    ]
