from django.db import models
import datetime


class Instruction(models.Model):
    instruction_theme = models.CharField('Тема:', max_length=200)
    instruction_author = models.ForeignKey('employees.Employee', on_delete=models.CASCADE,
                                           verbose_name='Автор инструкции:')
    instruction_create_date = models.DateField('Дата создания:', default=datetime.date.today())
    instruction_link = models.URLField('Ссылка на файл:', max_length=200)
    SearchableFields = ['instruction_theme', 'instruction_author__employee_name']

    def __str__(self):
        return self.instruction_theme

    class Meta:
        verbose_name = "Инструкция"
        verbose_name_plural = "Инструкции"
