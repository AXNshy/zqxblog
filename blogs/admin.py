from django.contrib import admin
from .models import Blog,Person
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'createTime', 'updateTime',)

# class PersonAdmin(admin.ModelAdmin):
#     list_display = ('fullName',)

# admin.site.register(Blog, ArticleAdmin)
# admin.site.register(Person,PersonAdmin)
admin.site.register(Blog)