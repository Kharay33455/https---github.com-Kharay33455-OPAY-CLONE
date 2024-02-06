# Generated by Django 5.0.1 on 2024-02-03 11:52

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_alter_bankuser_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankuser',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.uuid1, max_length=225, null=True, unique=True),
        ),
    ]
