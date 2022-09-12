from django.urls import path

from expense import views as v

app_name = 'expense'

urlpatterns = [
    path('', v.expense_list, name='url_expense_list'),
    path('<int:pk>/', v.expense_detail, name='url_expense_detail'),
    path('create/', v.expense_create, name='url_expense_create'),
    path('<int:pk>/update/', v.expense_update, name='url_expense_update'),
    path('<int:pk>/delete/', v.expense_delete, name='url_expense_delete'),


]
