# Generated by Django 4.2.7 on 2024-02-19 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='productdiscription',
        ),
    ]
