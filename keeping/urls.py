from django.urls import path

from keeping.views import ListExpense

app_name = 'keeping'


urlpatterns = [
    path('list/', ListExpense.as_view())
]
