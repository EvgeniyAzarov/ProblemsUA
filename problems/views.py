from django.shortcuts import render
from .models import Problem


def index(request):
    problems = Problem.objects.all()
    context = {'problems_list': problems}
    return render(request,
                  template_name='problems/index.html',
                  context=context)
