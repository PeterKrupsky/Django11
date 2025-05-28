from django.db import models


class Program_model(models.Model):
    task = models.CharField(
        verbose_name="Впишите нужную фразу",
        default="Информация",
        max_length=255,
    )
    a = models.CharField(
        verbose_name="Значение",
        default='Обо мне',
        max_length=255,

    )
    result = models.CharField(
        verbose_name="Результат",
        default="Результат",
        max_length=255,
    )
    current_date = models.DateTimeField(
        verbose_name="Дата изменения(save)", auto_now=True
    )

    def __str__(self):
        return f"self.task:{self.task}"

    class Meta:
        verbose_name = " Таблица результатов"
        verbose_name_plural = "Таблицы результатов"
        ordering = ("-pk", )


