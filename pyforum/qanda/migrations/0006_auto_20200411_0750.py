# Generated by Django 3.0.3 on 2020-04-11 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qanda', '0005_auto_20200411_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
