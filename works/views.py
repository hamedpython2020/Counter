from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from works.forms import ProjectForm, DocForm, ServicesForm


# @login_required
from works.models import project


def Newproject(request):
    if request.method == 'POST':
        project = ProjectForm(request.POST)
        if project.is_valid():
            project.save()
            return HttpResponseRedirect(reverse('works:services_new'))
        context = {}
        pass
    else:
        project = ProjectForm()
        context = {
            'project': project
        }
    return render(request, 'works/new_project.html', context)
    pass


def Projectlist(request):
    try:
        projects = project.objects.all().order_by('add_time')
        projects_c = projects.count()
        context = {
            'projects': projects,
            'projects_c': projects_c
        }
    except:
        error = 'Something went wrong'
        context = {
            'error': error
        }
    return render(request, 'works/project_list.html', context)

# @login_required
def Docupload(request):
    if request.method == 'POST':
        document = DocForm(request.POST, request.FILES)
        if document.is_valid():
            document.save()
            return HttpResponseRedirect(reverse('index'))
        context = {}
        pass
    else:
        document = DocForm()
        context = {
            'document': document
        }
    return render(request, 'works/upload_doc.html', context)
    pass


# @login_required
def NewService(request):
    if request.method == 'POST':
        service = ServicesForm(request.POST, request.FILES)
        if service.is_valid():
            service.save()
            return HttpResponseRedirect(reverse('index'))
        context = {}
        pass
    else:
        service = ServicesForm()
        context = {
            'service': service
        }
    return render(request, 'works/service_new.html', context)
    pass
