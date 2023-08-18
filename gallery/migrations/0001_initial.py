# Generated by Django 4.2 on 2023-04-09 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InstagramPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('post_id', models.CharField(max_length=255)),
                ('publish_date', models.DateTimeField(blank=True, null=True)),
                ('likes_count', models.IntegerField(blank=True, null=True)),
                ('image_url', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Пост из инстаграмм',
                'verbose_name_plural': 'Посты из инстаграмма',
            },
        ),
    ]
