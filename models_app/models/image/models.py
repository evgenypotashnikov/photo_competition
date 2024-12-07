from django.db import models


class Image(models.Model):
    file = models.ImageField(
        upload_to="images/file/%Y/%m/%d/", verbose_name="Изображение"
    )
    is_active = models.BooleanField(default=False, verbose_name="Активная?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    post = models.ForeignKey(
        "Post", on_delete=models.CASCADE, related_name="images", verbose_name="Пост"
    )

    def __str__(self):
        return f"id {self.id}"

    class Meta:
        db_table = "images"
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
