from django.db import models

choices = [
    ('Генеральный директор', 'Генеральный директор'),
    ('Главный бухгалтер', 'Главный бухгалтер'),
    ('Исполнительный директор', 'Исполнительный директор')
]


class Employee(models.Model):
    employee_name = models.CharField('ФИО:', max_length=200)
    employee_birthdate = models.DateField('Дата рождения:', blank=True)
    employee_post = models.CharField('Должность сотрудника:', choices=choices, max_length=200)

    def __str__(self):
        return self.employee_name

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
