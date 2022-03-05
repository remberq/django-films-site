from django.contrib import admin

# Register your models here.
from main.models import *

admin.site.register(Films)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(FimShots)
admin.site.register(RatingStar)
admin.site.register(Ratio)
admin.site.register(Reviews)
