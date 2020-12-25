from django.contrib import admin
from .models import *

# Register your models here.

class IdeasRating(admin.ModelAdmin):
    list_display = ('id','title','rating')
    list_display_links = ('title',)

admin.site.register(Ideas,IdeasRating)
admin.site.register(Photo)




admin.site.register(Rating)