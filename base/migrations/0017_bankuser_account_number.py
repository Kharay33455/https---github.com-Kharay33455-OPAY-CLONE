# Generated by Django 5.0.1 on 2024-01-31 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_bankuser_account_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankuser',
            name='account_number',
            field=models.IntegerField(default=11111111111),
            preserve_default=False,
        ),
    ]
