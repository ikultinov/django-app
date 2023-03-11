from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True,
                              verbose_name='Изображение')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='Тематика')
    articles = models.ManyToManyField(Article, related_name='tags',
                                      through='Scope')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Тематики'


class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    is_main = models.BooleanField(default=False, verbose_name='основной')

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'
        ordering = ['-is_main', '-tag']
