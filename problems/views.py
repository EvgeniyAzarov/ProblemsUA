from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Problem


def index(request):
    return redirect('problems_list')


def problems_list(request, per_page=10):
    problems = Problem.objects.all()
    paginator = Paginator(problems, per_page)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request,
                  template_name='problems/index.html',
                  context=context)
