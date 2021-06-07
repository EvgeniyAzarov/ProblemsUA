import json
import os
import tempfile
from datetime import date
from subprocess import Popen, PIPE

from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q, When, Case
from django.template.loader import get_template

from .models import Problem, Source, Attribute


def index(request):
    return redirect('problems_list')


def problems_list(request, per_page=10):
    context = {}
    filter_context = {}
    query = Q()

    search_text = request.GET.get('search_text')
    if search_text:
        context['search_text'] = search_text
        query &= (Q(text__icontains=search_text) | Q(name__contains=search_text))

    source_id = request.GET.get('source_id')
    if source_id and source_id != "0":
        source_id = int(source_id)
        filter_context['selected_source_id'] = source_id
        query &= Q(source__id=source_id)

    filter_context['selected_attributes'] = list(Attribute.objects.all().values_list('id', flat=True))
    selected_attributes = request.GET.getlist('selected_attributes', None)
    if selected_attributes:
        selected_attributes = list(map(int, selected_attributes))
        query &= Q(attributes__in=selected_attributes)
        filter_context['selected_attributes'] = selected_attributes

    problems = Problem.objects.filter(query).distinct().order_by('id')
    paginator = Paginator(problems, per_page)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context['page_obj'] = page_obj

    sources = Source.objects.all()
    filter_context['sources'] = sources
    attributes = Attribute.objects.all()
    filter_context['attributes'] = attributes

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


def get_problems_by_ids(pk_list):
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(pk_list)])
    problems = Problem.objects.filter(id__in=pk_list).order_by(preserved)
    return problems


def compile_paper_page(request):
    if request.method == 'POST':
        selected_problems = json.loads(request.body)['selectedProblems']
        pk_list = list(map(int, selected_problems.split()))
        problems = get_problems_by_ids(pk_list)
        context = {'problems': problems}
        return render(request, template_name='problems/compile_problems_list.html', context=context)
    else:
        return render(request, template_name='problems/compile_paper.html')


def get_compiled_paper(request):
    if request.method == 'POST':
        selected_problems = request.POST.get('selectedProblems')
        paper_title = request.POST.get('paperTitle')

        pk_list = list(map(int, selected_problems.split()))
        problems = get_problems_by_ids(pk_list)
        context = {
            'paper':
                {
                    'title': paper_title,
                    'problems': problems,
                }
        }

        template = get_template('paper_template.tex')
        rendered_tpl = template.render(context).encode('utf-8')

        if 'getTexButton' in request.POST:
            response = HttpResponse(rendered_tpl)
            response['Content-Disposition'] = \
                f"attachment; " \
                f"filename=problems_paper_{date.today().strftime('%d_%m_%y')}.tex"
        elif 'getPdfButton' in request.POST:
            with tempfile.TemporaryDirectory() as tempdir:
                process = Popen(
                    ['pdflatex', '-output-directory',  tempdir],
                    stdin=PIPE,
                    stdout=PIPE,
                )
                process.communicate(rendered_tpl)
                with open(os.path.join(tempdir, 'texput.pdf'), 'rb') as f:
                    pdf = f.read()
            response = HttpResponse(pdf, content_type='application/pdf')
        else:
            raise Http404()

        return response
    else:
        raise Http404()
