from django.contrib import admin

from models_app.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "username",
        "first_name",
        "last_name",
        "avatar",
        "is_staff",
        "is_active",
        "date_joined",
    ]
    list_display_links = [
        "id",
        "username",
        "first_name",
        "last_name",
    ]
    fieldsets = [
        (None, {"fields": ["id"]}),
        ("Логин и пароль", {"fields": ["username", "password"]}),
        ("Профиль пользователя", {"fields": ["avatar", "first_name", "last_name"]}),
        ("Статусы", {"fields": ["is_staff", "is_active"]}),
        ("Дата", {"fields": ["last_login", "date_joined"]}),
    ]
    readonly_fields = [
        "id",
        "date_joined",
        "last_login",
    ]
    list_filter = [
        "is_staff",
        "is_active",
    ]
    search_fields = [
        "id",
        "username",
        "first_name",
        "last_name",
    ]
