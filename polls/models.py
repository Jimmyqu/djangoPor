from django.db import models
from django.utils import timezone
import datetime


# Create your models here.

class Question(models.Model):  # 一个模型就是一张表
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('日期')  # Field的第一个参数来指定一个人类可读的名字

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text  # 让管理站点默认显示 字段为标题


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
