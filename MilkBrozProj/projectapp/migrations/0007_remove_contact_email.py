# Generated by Django 4.0.5 on 2022-07-05 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0006_alter_contact_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
    ]