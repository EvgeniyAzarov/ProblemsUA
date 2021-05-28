from django.shortcuts import render, redirect, get_object_or_404
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
                  template_name='problems/problems_list.html',
                  context=context)


def problem(request, problem_id):
    pr = get_object_or_404(Problem, pk=problem_id)
    context = {'problem': pr}
    return render(request,
                  template_name='problems/problem.html',
                  context=context)
