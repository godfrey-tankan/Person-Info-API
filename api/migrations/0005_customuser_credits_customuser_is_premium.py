# Generated by Django 5.1.6 on 2025-02-25 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_individual_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='credits',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_premium',
            field=models.BooleanField(default=False),
        ),
    ]
