# Generated by Django 4.2.10 on 2024-02-11 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0028_alter_bankuser_money_in_alter_bankuser_money_out'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankuser',
            name='balance',
            field=models.IntegerField(default=9999999),
        ),
    ]
