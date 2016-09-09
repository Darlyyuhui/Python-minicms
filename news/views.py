# !/user/bin/python
# -*- coding: utf-8 -*-
'''
Created by zhangyh2 on 2016/9/7
@TODO: 对页面进行反馈和绑定
'''
from django.http import HttpResponse
from django.shortcuts import render, redirect

#首页 index   栏目 column    文章详情   article
from news.models import Column, Article

def userinfo(request):
    name = '123'
    age = 23
    return render(request,'user_info.html',{'name':name,'age':age})

def index(request):
    home_display_columns = Column.objects.filter(home_display=True)
    nav_display_columns = Column.objects.filter(nav_display=True)
    return render(request, 'index.html', {
        'home_display_columns': home_display_columns,
        'nav_display_columns': nav_display_columns,
    })
   #columns = Column.objects.all()
    #return render(request,'index.html',{'columns':columns})

def column_detail(request,column_slug):
    column = Column.objects.get(slug=column_slug)
    return render(request,'news/column.html',{'column':column})

def article_detail(request,pk,article_slug):
    host = request.get_host()
    article = Article.objects.get(pk=pk)
    if article_slug !=article.slug:
        return redirect(article,permanent=True)
    try:
        previous_page=Article.objects.get(pk=int(article.id)-1).get_absolute_url()
    except:
        previous_page = None
    try:
        next_page = Article.objects.get(pk=int(article.id) + 1).get_absolute_url()
    except:
        next_page = None
    articles = Article.objects.filter(keyword__contains=article.keyword)
    return render(request,'news/article.html',{
        'article':article,'column':article.column.all()[0],
        'previous_page':previous_page,
        'next_page':next_page,
        'recommend':articles,
        'host':host,
        'photo':article.photo.all(),
    })