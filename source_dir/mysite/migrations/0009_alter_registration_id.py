# Generated by Django 4.2.13 on 2024-05-29 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_remove_registration_slug_registration_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
