# Generated by Django 4.2.13 on 2024-05-29 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_remove_registration_id_alter_registration_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='slug',
        ),
        migrations.AddField(
            model_name='registration',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
