# Generated by Django 4.1.3 on 2022-11-01 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinalProject', '0008_alter_post_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about',
            field=models.CharField(default='null', max_length=500),
        ),
    ]
