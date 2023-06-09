# Generated by Django 4.2.1 on 2023-06-03 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_formulation', models.CharField(max_length=200, verbose_name='Формулировка вопроса:')),
                ('question_answer', models.CharField(max_length=200, verbose_name='Ответ на вопрос:')),
                ('question_theme', models.CharField(choices=[('Финансы', 'Финансы'), ('Продажи', 'Продажи'), ('Маркетинг', 'Маркетинг')], max_length=200)),
                ('question_link', models.URLField(verbose_name='Ссылка на файл:')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
    ]
