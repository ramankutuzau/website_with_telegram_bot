from django.db import models


# Create your models here.
class InstagramPost(models.Model):
    is_active = models.BooleanField(default=True)
    post_id = models.CharField(max_length=255,blank=True,null=True)
    post_url = models.CharField(max_length=255,blank=True,null=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    likes_count = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='instagram-posts/',blank=True,null=True)

    def __str__(self):
        return f"InstagramPost {self.post_id} лайков {self.likes_count}"

    class Meta:
        verbose_name = 'Пост из инстаграмм'
        verbose_name_plural = 'Посты из инстаграмма'
