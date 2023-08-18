from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField


class Category(MPTTModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey(
        'self',
        related_name='children',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='articles/')
    text = RichTextField()

    category = models.ForeignKey(
        Category,
        related_name='product',
        on_delete=models.SET_NULL,
        null=True
    )
    slug = models.SlugField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_single', kwargs={'slug': self.category.slug, 'product_slug': self.slug})

    class Meta:
        verbose_name = 'Пост для блога'
        verbose_name_plural = 'Посты для блога'


class Comment(models.Model):
    name = models.CharField(max_length=50)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name