from django.contrib import admin

# Register your models here.
from works.models import project, p_document, Services

admin.site.register(project)
admin.site.register(p_document)
admin.site.register(Services)
