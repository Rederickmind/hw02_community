from django.shortcuts import render, get_object_or_404
from .models import Post, Group
from django.core.paginator import Paginator


def index(request):
    """Главная страница"""
    posts = Post.objects.all()
    # Показывать по 10 записей на странице.
    paginator = Paginator(posts, 10)

    # Из URL извлекаем номер запрошенной страницы
    page_number = request.GET.get('page')

    # Получаем набор записей для страницы с запрошенным номером
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }

    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    """Получение постов нужной группы по запросу"""
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    # Показывать по 10 записей на странице.
    paginator = Paginator(posts, 10)

    # Из URL извлекаем номер запрошенной страницы
    page_number = request.GET.get('page')

    # Получаем набор записей для страницы с запрошенным номером
    page_obj = paginator.get_page(page_number)

    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_list.html', context)
