#-*- coding: utf8 -*-
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage,InvalidPage #分页 3错误提示
from models import *
# Create your views here.

def getPage(req,articles):
    pn = req.GET.get('pn',None)
    pagintor = Paginator(articles,2) #第二个参数控制每页记录条数
    try:
        articles = pagintor.page(pn)  #第几页记录
    except(PageNotAnInteger,EmptyPage,InvalidPage),e:
        articles = pagintor.page(1)
    return articles

def index(req):

    articles = Article.objects.all()
    articles = getPage(req, articles)

    return render(req, 'index.html', locals())

@login_required(login_url='login')
def delete(req):
    did = req.GET.get('did', None)
    articles = Article.objects.all().filter(id=did)
    articles.delete()
    return HttpResponseRedirect('index')


def article(req):
    if req.method == 'POST':
        aid = req.GET.get('aid', None)
        su = Article.objects.get(id=aid)
        su.content = req.POST.get('tex')
        su.save()
    aid = req.GET.get('aid', None)
    article = Article.objects.get(id=aid)

    return render(req, 'article.html', locals())

def add(req):
    if req.method == 'POST':
        print '----**-'
        Article.objects.create(
            title=req.POST.get('title'),
            desc=req.POST.get('desc'),
            content=req.POST.get('content'),
            link=req.POST.get('link'),
        )
        return HttpResponseRedirect('/')

    return render(req, 'add.html',locals())

def login_x(req):
    if req.method == 'GET':
        return render(req,'login.html')
    else:
        print req.POST
        username = req.POST.get('username')

        password = req.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(req, user)
            return HttpResponseRedirect('article')
        else:
            return render(req,'login.html',{'log_err':"用户名或密码错误"})

def logout_x(req):
    logout(req)
    return HttpResponseRedirect(req.META['HTTP_REFERER'])