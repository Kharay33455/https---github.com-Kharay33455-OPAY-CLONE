# Generated by Django 5.0.1 on 2024-01-21 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_owner_balance_remove_owner_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]