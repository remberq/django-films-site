from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from main.models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class FilmsAdminForm(forms.ModelForm):
    """Add ckeditor form to film description field"""
    description = forms.CharField(
        label='Описание', widget=CKEditorUploadingWidget()
    )

    class Meta:
        model = Films
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'name')
    list_display_links = ("name", 'url')
    prepopulated_fields = {'url': ('name',)}


class ReviewInLine(admin.TabularInline):
    """add all film reviews to films panel"""
    model = Reviews
    extra = 1  # <-- add extra form to add new review
    readonly_fields = ('name', 'email')


class FilmShotsInline(admin.TabularInline):
    """add shots to film panel"""
    model = FimShots
    extra = 1
    readonly_fields = ('get_image',)  # <-- add image-preview to edit view

    def get_image(self, obj):
        """add to admin panel image-preview"""
        return mark_safe(f'<img src={obj.image.url} width="100" height="130"')

    get_image.short_description = 'Изображение'


@admin.register(Films)
class FilmsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'url', 'get_image', 'draft')
    list_display_links = ('id', 'title', 'url')
    list_filter = ('category', 'year')
    save_on_top = True
    search_fields = ('title', 'category__name')
    prepopulated_fields = {'url': ('title',)}  # <-- auto complete url field by title
    inlines = [FilmShotsInline, ReviewInLine]
    save_as = True  # <-- save copy in database as new object
    actions = ['published', 'unpublished']
    form = FilmsAdminForm  # <-- add ckeditor
    list_editable = ('draft',)
    fieldsets = (  # <-- make some fields inline
        ('Option 1', {
            'fields': (('title', 'tagline', 'url'),)
        }),
        (None, {
            'fields': ('description', ('poster', 'get_image'),)
        }),
        (None, {
            'fields': (('year', 'country'),)
        }),
        (None, {
            'fields': (('world_premiere', 'category', 'draft'),)
        }),
        (None, {
            'fields': (('budget', 'fees_in_russia', 'fees_in_world'),)
        }),
        ('Actors & Directors', {
            'classes': ('collapse',),  # <-- hide this group
            'fields': (('directors', 'actors', 'genres'),)
        }),
    )
    readonly_fields = ('get_image',)  # <-- add image-preview to edit view

    def get_image(self, obj):
        """add to admin panel image-preview"""
        return mark_safe(f'<img src={obj.poster.url} width="60" height="80"')

    get_image.short_description = 'Постер'

    """Action to admin panel"""

    def unpublished(self, request, queryset):
        """Unpublished film"""
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = '1 запись была обновлена'
        else:
            message_bit = f'{row_update} записей были обновлены'
        self.message_user(request, f'{message_bit}')

    def published(self, request, queryset):
        """Publish film"""
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = '1 запись была обновлена'
        else:
            message_bit = f'{row_update} записей были обновлены'
        self.message_user(request, f'{message_bit}')

    published.short_description = 'Опубликовать'
    published.allowed_permission = ('change',)
    unpublished.short_description = 'Убрать с публикации'
    unpublished.allowed_permission = ('change',)


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'movie', 'text', 'parent')
    list_display_links = ('name', 'email', 'movie', 'text', 'parent')
    search_fields = ('name', 'email', 'movie')
    readonly_fields = ('name', 'email')  # <--- can't edit field's


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_display_links = ('name', 'description')
    prepopulated_fields = {'url': ('name',)}


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'get_image')
    readonly_fields = ('get_image',)  # <-- add image-preview to edit view

    def get_image(self, obj):
        """add to admin panel image-preview"""
        return mark_safe(f'<img src={obj.photo.url} width="60" height="50"')

    get_image.short_description = 'Изображение'


@admin.register(FimShots)
class ShotsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'get_image', 'movie')
    model = Films
    readonly_fields = ('get_image',)  # <-- add image-preview to edit view

    def get_image(self, obj):
        """add to admin panel image-preview"""
        return mark_safe(f'<img src={obj.image.url} width="60" height="50"')

    get_image.short_description = 'Изображение'


admin.site.register(RatingStar)
admin.site.register(Ratio)

admin.site.site_title = 'Django Movies'
admin.site.site_header = 'Django Movies'
