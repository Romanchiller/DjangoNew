from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    ordering = 'group'
    object_list = Student.objects.all().prefetch_related('teachers').order_by(ordering)
    template = 'school/students_list.html'
    context = {'object_list' : object_list}

    return render(request, template, context)
