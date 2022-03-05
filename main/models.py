from django.urls import reverse
from django.utils.datetime_safe import date
from dynamic_image.fields import DynamicImageField
from django.db import models


class Category(models.Model):
    """Film category"""
    name = models.CharField('Категория', max_length=150)
    description = models.TextField(verbose_name='Описание')
    url = models.SlugField(max_length=160, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'


class Actor(models.Model):
    """Film actor's and producer's"""
    name = models.CharField('Имя', max_length=100)
    age = models.PositiveSmallIntegerField('Возраст', default=0)
    description = models.TextField('Описание')
    photo = DynamicImageField('Фотография')
    slug = models.SlugField('Url', db_index=True)

    def get_upload_to(self, field_name):
        """Make a dynamic path to images"""
        class_name = self.__class__.__name__.lower()
        instance_name = self.slug
        return f'{class_name}/{instance_name}'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Актеры'
        verbose_name = 'Актер'


class Genre(models.Model):
    """Films genre"""
    name = models.CharField('Жанр', max_length=100)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Жанры'
        verbose_name = 'Жанр'


class Films(models.Model):
    """Film"""
    title = models.CharField('Название', max_length=100)
    tagline = models.CharField('Слога', max_length=100, default='')
    description = models.TextField('Описание')
    poster = DynamicImageField('Постер')
    year = models.PositiveSmallIntegerField('Дата выхода', default=2019)
    country = models.CharField('Страна', max_length=30)
    directors = models.ManyToManyField('Actor', verbose_name='режиссер', related_name='film_director')
    actors = models.ManyToManyField('Actor', verbose_name='актеры', related_name='film_actor')
    genres = models.ManyToManyField('Genre', verbose_name='жанры')
    world_premiere = models.DateTimeField('Премьера в мире', auto_now=True)
    budget = models.PositiveIntegerField('Бюджет', default=0, help_text='сумма в долларах')
    fees_in_russia = models.PositiveIntegerField('Сборы в России', default=0, help_text='сумма в долларах')
    fees_in_world = models.PositiveIntegerField('Сборы в Мире', default=0, help_text='сумма в долларах')
    category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField('Черновик', default=False)

    def get_upload_to(self, field_name):
        """Make a dynamic path to images"""
        class_name = self.__class__.__name__.lower()
        instance_name = self.url
        return f'{class_name}/{instance_name}'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'slug': self.url})

    class Meta:
        verbose_name_plural = 'Фильмы'
        verbose_name = 'Фильм'


class FimShots(models.Model):
    """Film's shots"""
    title = models.CharField('Заголовок', max_length=100)
    description = models.TextField('Описание')
    image = DynamicImageField('Фотография')
    movie = models.ForeignKey('Films', verbose_name='Фильм', on_delete=models.CASCADE)
    shot_slug = models.SlugField('Url', max_length=100)

    def get_upload_to(self, field_name):
        """Make a dynamic path to images"""
        class_name = self.__class__.__name__.lower()
        instance_name = self.shot_slug
        return f'{class_name}/{instance_name}'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кадр из фильма'
        verbose_name_plural = 'Кадры из фильма'


class RatingStar(models.Model):
    """Film star's"""
    value = models.SmallIntegerField('Значение', default=0)

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'


class Ratio(models.Model):
    """Film rating's"""
    ip = models.CharField('IP адрес', max_length=15)
    star = models.ForeignKey('RatingStar', on_delete=models.CASCADE, verbose_name='звезда')
    movie = models.ForeignKey('Films', verbose_name='фильм', on_delete=models.CharField)

    def __str__(self):
        return f'{self.star} - {self.movie}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Reviews(models.Model):
    """Film review's"""
    email = models.EmailField('Email')
    name = models.CharField('Имя', max_length=100)
    text = models.TextField('Сообщение', max_length=5000)
    parent = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey('Films', verbose_name='фильм', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.movie}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
