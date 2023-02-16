from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from works.forms import ProjectForm, DocForm, ServicesForm


# @login_required
def Newproject(request):
    if request.method == 'POST':
        context = {}
        pass
    else:
        project = ProjectForm()
        context = {
            'project': project
        }
    return render(request, 'works/new_project.html', context)
    pass


# @login_required
def Docupload(request):
    if request.method == 'POST':
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
        context = {}
        pass
    else:
        service = ServicesForm()
        context = {
            'service': service
        }
    return render(request, 'works/service_new.html', context)
    pass
