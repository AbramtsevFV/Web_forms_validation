from django.db import models

class Template(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название шаблона')

    def __str__(self):
       return self.name

    class Meta:
        verbose_name = 'Шаблон'
        verbose_name_plural = 'Шаблоны'

class Field(models.Model):
    class Type:
        choices = (
                ('date', 'date'),
                 ('phone', 'phone'),
                 ('email', 'email'),
                 ('text', 'text'),
             )
    template = models.ForeignKey(Template, related_name='sample', verbose_name='Шаблон', on_delete=models.CASCADE)
    name_field = models.CharField(max_length=256, verbose_name='Имя поля')
    type_field = models.CharField(max_length=5, choices=Type.choices, verbose_name='Тип поля')

    def __str__(self):
        return self.name_field

    class Meta:
        verbose_name = 'Поле'
        verbose_name_plural = 'Поля'