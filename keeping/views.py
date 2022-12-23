from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from keeping.models import Expenses


class ListExpense(ListView):
    model = Expenses
    queryset = Expenses.objects.all()
    template_name = 'expenses/list.html'


class DetailExpense(DetailView):
    model = Expenses
    queryset = Expenses.objects.all()
    template_name = 'expenses/detail.html'


class CreateExpense(CreateView):
    template_name = 'expenses/create.html'
    success_url = ''
    form_class = ''


class UpdateExpense(UpdateView):
    template_name = 'expenses/create.html'
    success_url = ''
    form_class = ''
    model = Expenses


class DeleteExpense(DeleteView):
    template_name = 'expenses/delete.html'
    model = Expenses
    success_url = reverse_lazy('')
