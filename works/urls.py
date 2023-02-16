from django.urls import path
from works import views

app_name = 'works'

urlpatterns = [
    path('project/new/', views.Newproject, name='project_new'),
    path('documents/uplode/', views.Docupload, name='upload_doc')
]