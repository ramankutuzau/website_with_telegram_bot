# Generated by Django 4.2 on 2023-04-09 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instagrampost',
            name='image_url',
        ),
        migrations.AddField(
            model_name='instagrampost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='instagram-posts/'),
        ),
        migrations.AddField(
            model_name='instagrampost',
            name='post_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='instagrampost',
            name='post_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
