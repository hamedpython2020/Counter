from django import forms

from works.models import Services, project, p_document


class ServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['define_services', 'cost_services', 'description', 'project', 'date']
        pass
    pass


class ProjectForm(forms.ModelForm):
    class Meta:
        model = project
        exclude = []
        pass
    pass


class DocForm(forms.ModelForm):
    class Meta:
        model = p_document
        exclude = []
        pass
    pass
