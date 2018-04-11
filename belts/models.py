from django.db import models

class Belt(models.Model):
    
    class Meta():
        verbose_name="пояс"
        verbose_name_plural="поясов"

    DEPARTMENTS = (
        ('ЭРУ', 'ЭРУ'),
        ('ГШУ', 'ГШУ'),
        ('ГРП', 'ГРП'),
        ('связи', 'связи'),
        ('ППС', 'ППС'),
        ('энергетический', 'энергетический'),
        ('ЛЭУ', 'ЛЭУ'),
        ('ИЭТЛ', 'ИЭТЛ'),
        ('ВСП', 'ВСП'),
        ('котельные', 'котельные'),
    )
    department = models.CharField('участок', max_length=20, choices=DEPARTMENTS)

    TIPES = (
        ('пояс монтажный', 'пояс монтажный'),
        ('пояс страховочный', 'пояс страховочный'),
        ('веревка', 'веревка'),
    )
    tipe = models.CharField('тип', max_length=20, choices=TIPES)

    number = models.IntegerField('количество')

    data = models.DateField('срок сдачи')
