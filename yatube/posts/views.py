from django.shortcuts import render, get_object_or_404
from .models import Post, Group, User
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


# Функция для профиля пользователя
def profile(request, username):
    # Код запроса к модели User
    user = get_object_or_404(User, username=username)
    post_list = Post.objects.filter(author=user)
    post_quantity = post_list.count()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'user': user,
        'page_obj': page_obj,
        'post_quantity': post_quantity
    }
    return render(request, 'posts/profile.html', context)


# Функция для просмотра поста
def post_detail(request, post_id):
    # Код запроса к модели Posts
    post = get_object_or_404(Post, id=post_id)
    context = {
        'post': post
    }
    return render(request, 'posts/post_detail.html', context)
