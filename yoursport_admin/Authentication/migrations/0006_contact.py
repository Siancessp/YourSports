# Generated by Django 4.2.11 on 2024-04-10 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0005_pricing_gerneral_pricing_school_corporate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=1000)),
                ('message', models.TextField()),
            ],
        ),
    ]
