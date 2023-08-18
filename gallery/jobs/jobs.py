import asyncio
import datetime

from datetime import datetime

from django.core.files import File
from django.http import request
from instagram_private_api import Client, ClientCompatPatch
import urllib.request

import urllib.request
from datetime import datetime
from django.core.files import File
from gallery.models import InstagramPost
from config.settings import BASE_DIR, TELEGRAM_BOT_TOKEN
from telegram import Bot

def parse_instagram():
    try:
        # Введите свои данные вместо USERNAME и PASSWORD
        username = ''
        password = ''

        api = Client(username, password)
        user_info = api.username_info('')
        user_id = user_info['user']['pk']
        max_id = None

        while True:
            results = api.user_feed(user_id, max_id=max_id)
            items = results.get('items', [])
            for post in reversed(items):
                code = post.get('code')
                if code:
                    post_url = f'https://www.instagram.com/p/{code}/'

                image_versions = post.get('image_versions2')
                if image_versions:
                    # Если пост содержит изображение, загрузить его
                    image_url = image_versions['candidates'][0]['url']
                    # Сохраняем изображение в локальную директорию
                    post_id = post['id']
                    image_path = f"{BASE_DIR}/media/instagram-posts/{post_id}.jpg"
                    urllib.request.urlretrieve(image_url, image_path)

                    # Получить дату публикации и количество лайков
                    taken_at_timestamp = post['taken_at']
                    publish_date = datetime.fromtimestamp(taken_at_timestamp)
                    likes_count = post['like_count']

                    try:
                        existing_post = InstagramPost.objects.get(post_id=post_id)
                        existing_post.likes_count = likes_count
                        existing_post.save()
                        print(f'update {existing_post.pk}')
                    except InstagramPost.DoesNotExist:
                        new_post = InstagramPost(
                            post_id=post_id,
                            post_url=post_url,
                            publish_date=publish_date,
                            likes_count=likes_count,
                        )
                        with open(image_path, 'rb') as f:
                            django_file = File(f)
                            new_post.image.save(f"{post_id}.jpg", django_file)

                        new_post.save()
                        asyncio.run(send_sms_bot(f'Добавил новый пост {new_post.pk} '))

            if not results.get('has_next_page'):
                asyncio.run(send_sms_bot(f'Parser success'))
                break

            max_id = results.get('next_max_id')
    except Exception as e:
        asyncio.run(send_sms_bot(f"Parser error {e}"))


async def send_sms_bot(message):
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    await bot.send_message(chat_id="", text=message)
