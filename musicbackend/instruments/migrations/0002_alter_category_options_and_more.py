# Generated by Django 4.1.2 on 2023-04-25 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instruments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категории', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='img_for_instrument',
            options={'verbose_name': 'Фотографии муз инструментов', 'verbose_name_plural': 'Фотографии муз инструментов'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name': 'Подкатегории', 'verbose_name_plural': 'Подкатегории'},
        ),
    ]
