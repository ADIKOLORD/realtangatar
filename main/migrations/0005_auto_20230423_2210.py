# Generated by Django 2.2.12 on 2023-04-23 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20230423_2157'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mediacontent',
            options={'verbose_name': 'Контент События', 'verbose_name_plural': 'Контент Событий'},
        ),
        migrations.AlterModelOptions(
            name='mediatheme',
            options={'verbose_name': 'Тема События', 'verbose_name_plural': 'Темы Событий'},
        ),
        migrations.AlterField(
            model_name='teacher',
            name='birikme',
            field=models.CharField(choices=[('1', 'Табигый илимдер'), ('2', 'Кыргыз тили'), ('3', 'Орус тили'), ('4', 'Англис тили'), ('5', 'Физика'), ('6', 'Математика'), ('7', 'Технология')], max_length=30, verbose_name='Усулдук Бирикме'),
        ),
    ]
