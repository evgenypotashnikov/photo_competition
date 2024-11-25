from django.db import models


class Like(models.Model):
    user = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name="likes",
        verbose_name="Пользователь",
    )
    post = models.ForeignKey(
        "Post", on_delete=models.CASCADE, related_name="likes", verbose_name="Пост"
    )

    class Meta:
        db_table = "likes"
        unique_together = ["user", "post"]
        verbose_name = "Лайк"
        verbose_name_plural = "Лайки"
