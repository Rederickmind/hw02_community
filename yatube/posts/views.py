from django.shortcuts import render, get_object_or_404
from .models import Post, Group


# Количество отображаемых записей на странице
POSTS_AMOUNT = 10


def index(request):
    """Главная страница"""
    posts = Post.objects.all()[:POSTS_AMOUNT]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    """Получение постов нужной группы по запросу"""
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:POSTS_AMOUNT]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
