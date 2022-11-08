from django.contrib import admin
from .models import Post, Group


class PostAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group'
    )
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('text',)
    # Это позволит изменять поле group в любом посте
    list_editable = ('group',)
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date',)
    # Свойство для пустых полей
    empty_value_display = '-пусто-'


# При регистрации модели Post источником конфигурации для неё назначаем
# класс PostAdmin
admin.site.register(Post, PostAdmin)
admin.site.register(Group)
