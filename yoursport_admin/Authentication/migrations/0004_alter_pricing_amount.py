# Generated by Django 4.2.11 on 2024-04-10 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0003_pricing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricing',
            name='amount',
            field=models.BigIntegerField(),
        ),
    ]