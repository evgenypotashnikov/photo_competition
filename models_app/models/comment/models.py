from django.db import models


class Comment(models.Model):
    text = models.TextField(verbose_name="Сообщение")
    parent = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="comments",
        verbose_name="Родитель",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата редоктирования")
    post = models.ForeignKey(
        "Post",
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Пост",
    )
    user = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Пользователь",
    )
    is_answer = models.BooleanField(default=False, verbose_name="Это ответ?")

    class Meta:
        db_table = "comments"
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
