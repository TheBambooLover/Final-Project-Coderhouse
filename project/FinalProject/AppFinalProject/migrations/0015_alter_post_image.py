# Generated by Django 4.1.3 on 2022-11-04 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinalProject', '0014_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='posts'),
        ),
    ]
