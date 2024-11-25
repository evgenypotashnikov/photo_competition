from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата редоктирования")
    status = models.ForeignKey(
        "Status", on_delete=models.PROTECT, related_name="posts", verbose_name="Статус"
    )
    user = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="Пользователь",
    )

    class Meta:
        db_table = "posts"
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
