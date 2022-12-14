from django.shortcuts import redirect, render

from .forms import ExpenseForm
from .models import Expense


def expense_list(request):
    template_name = 'expense/expense_list.html'
    object_list = Expense.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)


def expense_detail(request, pk):
    template_name = 'expense/expense_detail.html'
    _object = Expense.objects.get(pk=pk)
    context = {'object': _object}
    return render(request, template_name, context)


def expense_create(request):
    template_name = 'expense/expense_form.html'
    form = ExpenseForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('expense:url_expense_list')

    context = {'form': form}
    return render(request, template_name, context)


def expense_update(request, pk):
    template_name = 'expense/expense_form.html'
    instance = Expense.objects.get(pk=pk)
    form = ExpenseForm(request.POST or None, instance=instance)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('expense:url_expense_list')

    context = {'form': form}
    return render(request, template_name, context)


def expense_delete(request, pk):
    template_name = 'expense/expense_confirm_delete.html'
    obj = Expense.objects.get(pk=pk)

    if request.method == 'POST':
        obj.delete()
        return redirect('expense:url_expense_list')

    context = {'object': obj}
    return render(request, template_name, context)
