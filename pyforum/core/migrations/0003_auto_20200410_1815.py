# Generated by Django 3.0.3 on 2020-04-10 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_vote'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]