from django.contrib import admin
from .models import *

# Register your models here.

class IdeasRating(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('title',)

admin.site.register(Ideas,IdeasRating)
admin.site.register(Photo)

admin.site.register(ICategory)


admin.site.register(Rating)