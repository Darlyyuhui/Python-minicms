from django.contrib import admin
from .models import Article, Column


class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'intro', 'nav_display', 'home_display')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','pub_date','update_time','published','image')

admin.site.register(Article,ArticleAdmin)
admin.site.register(Column,ColumnAdmin)