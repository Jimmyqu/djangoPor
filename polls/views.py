from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import Article, Choice
from django.views import generic


def index(request):
    # display_articles = Article.objects.filter(is_del=True) #筛选
    # display_articles = Article.objects.all() # 返回QUERYSET
    var_article = get_object_or_404(Article, id=1)  # 返回查询对象
    return render(request, 'index.html', {
        # 'content': display_articles,
        'var_article': var_article
    })
