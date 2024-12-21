# Generated by Django 5.1.3 on 2024-12-21 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='comments_media/')),
                ('img', models.FileField(blank=True, null=True, upload_to='comments_media/')),
                ('video', models.FileField(blank=True, null=True, upload_to='comments_media/')),
            ],
        ),
    ]
