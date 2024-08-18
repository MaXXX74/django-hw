from django.shortcuts import render
from django.views.generic import TemplateView


def task2_func(request):
    return render(request, 'second_task/func_template.html')


class task2_class(TemplateView):
    template_name = 'second_task/class_template.html'
