# Generated by Django 3.1.4 on 2021-03-09 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0005_auto_20210309_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='custom_key',
            field=models.CharField(default=models.AutoField(primary_key=True, serialize=False), max_length=24),
        ),
    ]
