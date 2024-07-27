from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from . forms import projectForm
from .models import Contact,Projects

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def resume(request):
    return render(request, 'resume.html')

def projects(request):
    images = Projects.objects.all()
    return render(request, 'projects.html', {'images': images})

def projectsUpload(request):
    if request.method == 'POST':
        form = projectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects_url')
    else:
        form = projectForm()
    return render(request, 'project_upload.html', {'form': form})


def projectUpdate(request, pk):
    image = get_object_or_404(Projects, pk=pk)
    if request.method == 'POST':
        form = projectForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('projects_url')
    else:
        form = projectForm(instance=image)
    return render(request, 'project_update.html', {'form': form})

def projectDelete(request,y):
	p=get_object_or_404(Projects ,pk=y)
	if request.method=="POST":
		p.delete()
		return redirect('projects_url')
	return render(request,"project_delete.html",{'h':p})



def contact(request):
    if request.method=='POST':
        uname=request.POST.get('name')
        uemail=request.POST.get('email')
        uphoneno=request.POST.get('num')
        umessage=request.POST.get('message')
        query=Contact(name=uname,email=uemail,phonenumber=uphoneno,message=umessage)
        query.save()
        messages.success(request,"Thanks for contacting us. We will get by you soon!")
    return render(request, 'contact.html')


   
