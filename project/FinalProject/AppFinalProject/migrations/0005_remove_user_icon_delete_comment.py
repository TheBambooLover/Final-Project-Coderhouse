# Generated by Django 4.1.3 on 2022-11-23 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinalProject', '0004_alter_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='icon',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
