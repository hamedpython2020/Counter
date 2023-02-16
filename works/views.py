from django.shortcuts import render

# Create your views here.
from works.forms import ProjectForm, DocForm


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
