# Generated by Django 4.1.2 on 2022-10-26 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinalProject', '0003_remove_post_comments_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='writter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppFinalProject.user'),
        ),
    ]