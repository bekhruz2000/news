from django.db import models
from django.urls import reverse


class News(models.Model):
    category = models.ForeignKey('Categories', verbose_name='Категория', on_delete=models.PROTECT, null=True)
    title = models.CharField(verbose_name='Название', max_length=150)
    content = models.TextField(verbose_name='Текст', blank=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)
    photo = models.ImageField(verbose_name='Фото', upload_to='news_poster/%Y/%m/%d/')
    is_published = models.BooleanField(verbose_name='Черновик', default=False)


    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse('new_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Categories(models.Model):
    title = models.CharField(verbose_name='Название категории', max_length=150, db_index=True)


    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse('get_categories', kwargs={'category_id': self.pk})
    

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'