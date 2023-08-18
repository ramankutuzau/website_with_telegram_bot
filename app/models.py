from django.db import models

# Create your models here.

class Projects(models.Model):
    image = models.ImageField(upload_to='main-slider/') # поле для загрузки картинки
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.pk} Cоздана : {self.created_at}'

    class Meta:
        verbose_name = 'Пост главной страницы'
        verbose_name_plural = 'Посты главной страницы'
