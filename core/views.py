from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from core.models import Post


@login_required(login_url='/login')
def index(request):
    if request.method == 'POST':
        if 'save' in request.POST:
            task = request.POST['task']
            if len(task) == 0:
                messages.Info(request, "Cmon not even one task to ignore!")
            else:
                new_task = Post.objects.create(
                    task=task,
                    user='root'
                )
                new_task.save()
        return render(request, 'index.html', {
            'tasks': Post.objects.filter(user='root')
        })

        # removing a task
    if request.method == "GET":
        # taking out all the tasks ids
        task_ids = [f"{task_id.id}" for task_id in Post.objects.filter(user='root')]
        for id in task_ids:
            if id in request.GET:
                Post.objects.filter(id=id).delete()  # deleting the object

    return render(request, 'index.html', {
        'tasks': Post.objects.filter(user='root')
    })


def login(request):
    if request.method == 'POST':
        username, password = request.POST['username'], request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Password is Wrong!")
            return redirect('login')

    return render(request, 'login.html')


@login_required(login_url='/login')
def logout(request):
    auth.logout(request)
    return redirect('login')
