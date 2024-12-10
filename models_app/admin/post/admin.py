from django.contrib import admin, messages
from django.core.exceptions import ValidationError
from django.shortcuts import redirect

from models_app.admin.image.admin import ImageInline
from models_app.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
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

    def save_model(self, request, obj, form, change):
        count_images = int(form.data.get("images-TOTAL_FORMS", 0))
        result = [
            form.data[f"images-{image}-is_active"]
            for image in range(count_images)
            if (
                not form.data.get(f"images-{image}-DELETE")
                and form.data.get(f"images-{image}-is_active")
            )
        ]
        if len(result) != 1:
            raise ValidationError("Нужно установить только одну активную фотографию")
        super().save_model(request, obj, form, change)
