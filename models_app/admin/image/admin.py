from django.contrib import admin

from models_app.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "post",
        "is_active",
        "created_at",
    ]
    list_display_links = [
        "id",
        "post",
    ]
    fieldsets = [
        (None, {"fields": ["id"]}),
        ("Фото поста", {"fields": ["file", "post"]}),
        ("Статус действия", {"fields": ["is_active"]}),
        ("Время", {"fields": ["created_at"]}),
    ]

    readonly_fields = [
        "id",
        "created_at",
    ]

    list_filter = [
        "is_active",
    ]
    search_fields = [
        "post__name",
    ]


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0
