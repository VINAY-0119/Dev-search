from django.shortcuts import render,redirect
from .models import Project
from .forms import ProjectForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def projects(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request,'projects/projects.html',context)

def project(request,pk):
    projectobj = Project.objects.get(id=pk)
    context = {'project':projectobj}
    return render(request,'projects/single-project.html',context)


@login_required(login_url='login')
def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('projects')
    context = {'form':form}
    return render(request,'projects/project-form.html',context)


@login_required(login_url='login')
def updateProject(request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance = project)
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES,instance = project)
        if form.is_valid():
            form.save()
            return redirect('projects')
        
    context ={'form':form}
    return render(request,'projects/project-form.html',context)


@login_required(login_url='login')
def deleteProject(request,pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object':project}
    return render(request,'projects/delete-template.html',context)

def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            print(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('projects')

        else:
            print(request, 'Username OR password is incorrect')

    return render(request,'projects/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')
