from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from works.forms import ProjectForm, DocForm, ServicesForm


# @login_required
from works.models import project, Services


def Newproject(request):
    if request.method == 'POST':
        project = ProjectForm(request.POST)
        if project.is_valid():
            project.save()
            return HttpResponseRedirect(reverse('works:services_new'))
        else:
            context = {
                'errors': "Something went wrong"
            }
    else:
        project = ProjectForm()
        context = {
            'project': project
        }
    return render(request, 'works/new_project.html', context)


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


def NewService(request):
    if request.method == 'POST':
        service = ServicesForm(request.POST, request.FILES)
        if service.is_valid():
            service = service.save()
            cost_service = service.cost_services
            customer = service.manager
            customer.spend(cost_service)
            customer.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            context = {
                'error': 'Something went wrong'
            }
    else:
        service = ServicesForm()
        context = {
            'service': service
        }
    return render(request, 'works/service_new.html', context)


def Servicelist(request):
    try:
        service = Services.objects.all().order_by('date')
        service_c = service.count()
        context = {
            'service': service,
            'service_c': service_c
        }
    except:
        error = 'Something went wrong'
        context = {
            'error': error
        }
    return render(request, 'works/service_list.html', context)
