from django.contrib import admin
from .models import Question, Choice


# Register your models here.

class QuestionAdmin(admin.ModelAdmin):  # 改变管理界面布局
    fields = ['pub_date', 'question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
