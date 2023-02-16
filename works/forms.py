from django import forms

from works.models import Services, project, p_document


class ServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['define_services', 'cost_services', 'description', 'project', 'date']
        pass
    # years = []
    # for i in range(1330, 1420):
    #     years.append(str(i))
    #     pass
    # months = {1: 'فروردین', 2: 'اردیبهشت', 3: 'خرداد',
    #           4: 'تیر', 5: 'مرداد', 6: 'شهریور',
    #           7: 'مهر', 8: 'آبان', 9: 'آذر',
    #           10: 'دی', 11: 'بهمن', 12: 'اسفند'
    #           }
    # date = forms.DateField(label="تاریخ ثبت", widget=forms.SelectDateWidget(years, months))
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
