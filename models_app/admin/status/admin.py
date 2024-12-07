from django.contrib import admin

from models_app.models import Status


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
    ]
    list_display_links = [
        "id",
        "title",
    ]
    fields = [
        "id",
        "title",
    ]

    readonly_fields = [
        "id",
    ]
