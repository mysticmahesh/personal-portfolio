from django.urls import path
from personal_portfolio_app import views

urlpatterns = [
    path('', views.home,name='home_url'),
    path('about', views.about,name='about_url'),
    path('resume', views.resume,name='resume_url'),
    path('projects', views.projects,name='projects_url'),
    path('project_upload', views.projectsUpload,name='project_upload_url'),
    path('project_update/<int:pk>/', views.projectUpdate,name='project_update_url'),
    path('project_delete/<int:y>/', views.projectDelete,name='project_delete_url'),
    path('contact', views.contact,name='contact_url'),

]