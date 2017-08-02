from django.shortcuts import render

from test.models import Article


def article(request):
    articles = Article.objects.all()
    return render(request, 'test/comments.html', {'articles': articles})
