from django.contrib import admin

from models_app.models import Like


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "user",
        "post",
    ]
    list_display_links = [
        "id",
    ]
    fieldsets = [
        (None, {"fields": ["id"]}),
        ("Идентификатор участника и поста", {"fields": ["user", "post"]}),
    ]

    readonly_fields = [
        "id",
    ]
