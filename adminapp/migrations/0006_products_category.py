# Generated by Django 4.2.7 on 2024-03-05 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0005_delete_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.CharField(default='', max_length=10),
        ),
    ]
