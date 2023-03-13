from django.urls import path

from keeping.views import ListExpense, DeleteExpense, CreateExpense

app_name = 'keeping'


urlpatterns = [
    path('list/', ListExpense.as_view(), name='list'),
    path('create/', CreateExpense.as_view(), name='create'),
    path('delete/<int:pk>', DeleteExpense.as_view())
]
