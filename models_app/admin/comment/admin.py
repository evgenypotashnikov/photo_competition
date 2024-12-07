from django.contrib import admin

from models_app.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "parent",
        "updated_at",
        "created_at",
    ]
    list_display_links = [
        "id",
        "user",
        "parent",
    ]
    fieldsets = [
        (None, {"fields": ["id"]}),
        ("Тело сообщения", {"fields": ["text", "is_answer"]}),
        ("Идентификаторы", {"fields": ["parent", "post", "user"]}),
        ("Время", {"fields": ["updated_at", "created_at"]}),
    ]

    readonly_fields = [
        "id",
        "created_at",
        "updated_at",
    ]
