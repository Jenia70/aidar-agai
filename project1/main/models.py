from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=60)
    task = models.TextField('Описание')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'