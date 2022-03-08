# Generated by Django 4.0.3 on 2022-03-08 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_films_options_alter_ratingstar_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='actor',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='actor',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='actor',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='category',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='category',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='films',
            name='country_en',
            field=models.CharField(max_length=30, null=True, verbose_name='Страна'),
        ),
        migrations.AddField(
            model_name='films',
            name='country_ru',
            field=models.CharField(max_length=30, null=True, verbose_name='Страна'),
        ),
        migrations.AddField(
            model_name='films',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='films',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='films',
            name='tagline_en',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='Слога'),
        ),
        migrations.AddField(
            model_name='films',
            name='tagline_ru',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='Слога'),
        ),
        migrations.AddField(
            model_name='films',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='films',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='fimshots',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='fimshots',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='fimshots',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='fimshots',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='genre',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='genre',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='genre',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Жанр'),
        ),
        migrations.AddField(
            model_name='genre',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Жанр'),
        ),
    ]