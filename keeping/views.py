from datetime import datetime
from calendar import monthrange
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from keeping.forms import ExpenseForm
from keeping.models import Expenses


class ListExpense(ListView):
    model = Expenses
    context_object_name = 'expenses'
    queryset = Expenses.objects.all()
    template_name = 'expenses/datelist.html'
    # template_name = 'expenses/list.html'

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        date = datetime.now()
        start_cont = datetime(date.year, date.month-1, 1, 0, 0, 0, 0)
        weekday, end_day = monthrange(date.year, date.month-1)
        end_cont = datetime(date.year, date.month-1, end_day, 0, 0, 0, 0)
        return context_data

    def get_queryset(self):
        # if self.request.GET.get('end_date') and self.request.GET.get('start_date'):
        #     queryset = super().get_queryset()
        #     queryset = queryset.filter(date__lte=self.request.GET.get('end_date'),
        #                                date__gte=self.request.GET.get('start_date'))
        #     return queryset
        # else:
        #     return ValueError

        queryset = super().get_queryset()
        queryset = queryset.filter(date__lte=self.request.GET.get('end_date'),
                                   date__gte=self.request.GET.get('start_date'))
        return queryset


class DetailExpense(DetailView):
    model = Expenses
    queryset = Expenses.objects.all()
    template_name = 'expenses/detail.html'


class CreateExpense(CreateView):
    template_name = 'expenses/create.html'
    success_url = reverse_lazy('keeping:list')
    form_class = ExpenseForm


class UpdateExpense(UpdateView):
    template_name = 'expenses/create.html'
    success_url = reverse_lazy('keeping:list')
    form_class = ExpenseForm
    model = Expenses


class DeleteExpense(DeleteView):
    template_name = 'expenses/delete.html'
    model = Expenses
    success_url = reverse_lazy('keeping:list')
