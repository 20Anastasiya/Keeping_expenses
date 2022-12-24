from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}'


class Expenses(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория',
        db_index=True,
        blank=False,
        null=False
    )
    description = models.CharField(max_length=500, verbose_name='Описание')
    amount = models.DecimalField(verbose_name='Сумма', decimal_places=2, max_digits=2)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    class Meta:
        verbose_name = 'Расходы'
        verbose_name_plural = 'Расходы'

    def __str__(self):
        return f'{self.category}{self.amount}{self.date}'
