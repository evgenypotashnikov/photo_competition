from cfgv import ValidationError
from django.contrib import admin

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
        count = 0

        count_images = int(form.data.get("images-TOTAL_FORMS", 0))
        for image in range(count_images):
            count_active = form.data.get(f"images-{image}-is_active", None)
            is_delete = form.data.get(f"images-{image}-DELETE", None)
            if count_active == "on" and not is_delete:
                count += 1
                if count > 1:
                    raise ValidationError(
                        {
                            "is_active": [
                                "Нельзя установить более одной активной фотографии"
                            ]
                        }
                    )
        super().save_model(request, obj, form, change)
