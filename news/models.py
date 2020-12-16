from django.db import models


class Articles(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    full_text = models.TextField('Текст записи', max_length=8000)
    date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'


    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'




