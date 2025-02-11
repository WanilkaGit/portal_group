# Generated by Django 5.1.3 on 2024-12-21 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_system', '0002_topic_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/forum/'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='title',
            field=models.CharField(max_length=72),
        ),
    ]
