from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):  # 一个模型就是一张表
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    created_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING,default=1)
    is_del = models.BooleanField(default=False)
    read_num = models.IntegerField(default=0)

    def __str__(self):
        return self.title  # 让管理站点默认显示 字段为标题


class Choice(models.Model):
    question = models.ForeignKey(Article)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
