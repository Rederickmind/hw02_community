from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    """Главная страница"""
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    """Получение постов нужной группы по запросу"""
    POSTS_AMOUNT = 10
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:POSTS_AMOUNT]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
