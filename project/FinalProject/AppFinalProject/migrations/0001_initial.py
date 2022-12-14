# Generated by Django 4.1.3 on 2022-11-15 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writter', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('text', models.TextField(max_length=300)),
                ('image', models.ImageField(null=True, upload_to='djangouploads/postuploads/images')),
                ('posted_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=18)),
                ('password', models.CharField(max_length=22)),
                ('email', models.CharField(max_length=300)),
                ('icon', models.ImageField(null=True, upload_to='djangouploads/useruploads/images')),
                ('about', models.CharField(max_length=500, null=True)),
                ('writter', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
                ('post', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='AppFinalProject.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppFinalProject.user')),
            ],
        ),
    ]
