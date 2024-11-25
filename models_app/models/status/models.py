from django.db import models


class Status(models.Model):
    title = models.CharField(max_length=255, verbose_name="Статус")

    class Meta:
        db_table = "statuses"
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"
