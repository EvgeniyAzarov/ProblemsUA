from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Problem, Source


def index(request):
    return redirect('problems_list')


def problems_list(request, per_page=10):
    context = {}
    filter_context = {}
    problems = Problem.objects

    search_text = request.GET.get('search_text')
    if search_text:
        search_text.strip()
        context['search_text'] = search_text
        problems = problems \
            .filter(Q(text__icontains=search_text) | Q(name__contains=search_text))

    source_id = request.GET.get('source_id')
    if source_id:
        source_id = int(source_id)
        filter_context['selected_source_id'] = source_id
        problems = problems.filter(source__id=source_id)

    problems = problems.order_by('id')
    paginator = Paginator(problems, per_page)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context['page_obj'] = page_obj

    sources = Source.objects.all()
    filter_context['sources'] = sources

    context['filter'] = filter_context

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
