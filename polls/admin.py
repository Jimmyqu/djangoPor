from django.contrib import admin
from .models import Article, Choice


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):  # 改变管理界面布局
    #  fields = ['title', 'content',]  # 设置可编辑字段

    list_display = ('id', 'title', 'content','created_time','is_del','author')  # 管理界面显示的表字段


admin.site.register(Article, ArticleAdmin)
admin.site.register(Choice)
