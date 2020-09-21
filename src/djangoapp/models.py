from django.db import models
from django.utils import timezone

# Create your models here.

class BoardModel(models.Model):
    title = models.CharField(verbose_name='危険箇所の場所', max_length=50)
    content = models.TextField(verbose_name='危険箇所である理由', max_length=100)
    author = models.CharField(verbose_name='投稿者', max_length=50)
    images = models.ImageField(verbose_name='画像', upload_to='')
    dangerous = models.IntegerField(verbose_name='危険度', null=True, blank=True, default=0)
    published_date = models.DateTimeField(verbose_name='投稿日',blank=True, null=True)

    def published(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = '豊川市内危険箇所一覧'
        verbose_name_plural = '豊川市内危険箇所一覧'
        ordering = ['-dangerous']