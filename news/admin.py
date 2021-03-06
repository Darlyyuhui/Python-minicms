from django.contrib import admin
from .models import Article, Column, Photo, Video

'''
后台展示选项
'''

class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'intro', 'nav_display', 'home_display')
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name','image',)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('name', 'path',)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','pub_date','update_time','image','keyword')
admin.site.register(Column,ColumnAdmin)
admin.site.register(Photo,PhotoAdmin)
admin.site.register(Video,VideoAdmin)
admin.site.register(Article,ArticleAdmin)
