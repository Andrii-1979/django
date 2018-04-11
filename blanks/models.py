from django.db import models

class Blank(models.Model):

    class Meta():
        verbose_name="бланк"
        verbose_name_plural="бланки"

    position = models.IntegerField('приоритет отображения', blank=True, null=True)
    title = models.CharField('название бланка', max_length=80)
    base = models.CharField('документ-основание', blank=True, null=True, max_length=40)
    doc = models.CharField('ссылка на doc', max_length=10, blank=True, null=True)
    pdf = models.CharField('ссылка на pdf', max_length=10, blank=True, null=True)
    
    def __str__(self):
        return self.title