# Generated by Django 4.2.1 on 2023-06-03 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_alter_employee_employee_post'),
        ('instructions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instruction',
            name='instruction_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee', verbose_name='Автор инструкции:'),
        ),
    ]
