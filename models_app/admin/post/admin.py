from django.contrib import admin

from models_app.admin.image.admin import ImageInline
from models_app.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    def save(self, obj):
        pass

    list_display = [
        "id",
        "name",
        "user",
        "status",
        "created_at",
    ]
    list_display_links = [
        "id",
        "name",
    ]
    fieldsets = [
        (None, {"fields": ["id"]}),
        ("Тело поста", {"fields": ["name", "description"]}),
        ("Пользователь", {"fields": ["user"]}),
        ("Статус поста", {"fields": ["status"]}),
        ("Время", {"fields": ["updated_at", "created_at"]}),
    ]

    readonly_fields = [
        "id",
        "created_at",
        "updated_at",
    ]

    list_filter = [
        "status",
    ]
    search_fields = [
        "id",
        "name",
        "username",
    ]
    inlines = [
        ImageInline,
    ]
