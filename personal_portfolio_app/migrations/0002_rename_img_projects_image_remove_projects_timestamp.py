# Generated by Django 5.0.6 on 2024-07-26 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal_portfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='img',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='timeStamp',
        ),
    ]
