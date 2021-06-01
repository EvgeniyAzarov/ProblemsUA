from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q, QuerySet
from .models import Problem


def index(request):
    return redirect('problems_list')


def problems_list(request, per_page=10):
    context = {}

    if request.method == "POST":
        search_text = request.POST['search_text']
        search_text.strip()
        if search_text:
            context['search_text'] = search_text
            problems = Problem.objects \
                .filter(Q(text__icontains=search_text) | Q(name__contains=search_text)) \
                .order_by('id')
        else:
            return redirect('problems_list')
    else:
        problems = Problem.objects.all().order_by('id')

    paginator = Paginator(problems, per_page)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context['page_obj'] = page_obj

    return render(request,
                  template_name='problems/problems_list.html',
                  context=context)


def problem(request, problem_id):
    pr = get_object_or_404(Problem, pk=problem_id)
    context = {'problem': pr}
    return render(request,
                  template_name='problems/single_problem.html',
                  context=context)


def compile_paper(request):
    return render(request, template_name='problems/compile_paper.html')


def test_page(request):
    return render(request, template_name='problems/test.html')
