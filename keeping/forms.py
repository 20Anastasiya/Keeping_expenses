from django import forms

from keeping.models import Category, Expenses


class ExpenseForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label='Категория*',
        help_text='Выбирете категорию',
        blank=False,
        widget=forms.widgets.Select(attrs={'size': 1}),
        required=False
    )
    description = forms.CharField(max_length=500, label='Описание*', help_text='Заполните описание',
                                  widget=forms.widgets.Textarea())
    amount = forms.DecimalField(min_value=1, label='Сумма*', required=False)
    date = forms.DateTimeField(label='Дата*', widget=forms.widgets.DateTimeInput(), required=False)

    class Meta:
        model = Expenses
        fields = ('category', 'description', 'amount', 'date')
