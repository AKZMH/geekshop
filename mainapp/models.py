from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название', unique=True)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.pk}. {self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name', )
