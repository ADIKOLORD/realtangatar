# Generated by Django 2.2.12 on 2023-05-02 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20230424_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('desc', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='banners/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Баннер',
                'verbose_name_plural': 'Баннер',
            },
        ),
        migrations.AlterModelOptions(
            name='mediacontent',
            options={'verbose_name': 'Фото-Видео', 'verbose_name_plural': 'Фото-Видео'},
        ),
        migrations.AlterModelOptions(
            name='mediatheme',
            options={'verbose_name': 'Мероприятия', 'verbose_name_plural': 'Мероприятия'},
        ),
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(upload_to='students/', verbose_name='Фото'),
        ),
    ]
