# Generated by Django 3.1.4 on 2021-03-09 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0006_lesson_custom_key'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['custom_key']},
        ),
    ]
