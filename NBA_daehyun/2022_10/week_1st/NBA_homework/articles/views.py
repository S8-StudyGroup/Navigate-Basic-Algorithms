from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from articles.forms import ArticleForm
from .models import Article
# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }

    return render(request, 'articles/index.html', context)


@login_required
def create(request):
    if request.method=="POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
            'form':form,
        }
    return render(request, 'articles/new.html', context)
    
    

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article.pk)

@login_required
def update(request, pk):
    if request.method=='POST':
        article = Article.objects.get(pk=pk)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    
    else:
        article = Article.objects.get(pk=pk)
        form = ArticleForm(instance=article)
    context = {
        'article' : article,
        'form':form
    }
    return render(request, 'articles/update.html', context)