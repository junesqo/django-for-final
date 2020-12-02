from django.db import models


class Course(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    category = models.CharField('Категория', max_length=100)
    description = models.TextField('Описание')
    link = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'