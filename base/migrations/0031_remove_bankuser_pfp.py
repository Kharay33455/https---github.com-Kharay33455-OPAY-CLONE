# Generated by Django 4.2.10 on 2024-02-11 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0030_bankuser_pfp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankuser',
            name='pfp',
        ),
    ]
