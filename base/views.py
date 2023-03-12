# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .serializers import TaskSerializer

# from .models import Tasks

# from django.contrib.auth.models import User


# # @api_view(['GET'])
# def getTasks(request):
#     tasks = Tasks.objects.all()
#     serialiser = TaskSerializer(tasks, many=True)
#     return Response(serialiser.data)

# # @api_view(['GET'])
# def getTask(request,pk):
#     user = User.objects.filter(id=pk).first()
#     task = Tasks.objects.filter(assigned=pk)
#     serialiser = TaskSerializer(task, many=True)
#     return Response(serialiser.data)

# # @api_view(['GET'])
# def test(request):
#     routes = {
#         'naman':'na',
#         'mait':'ma'
#     }
#     return Response(routes)

from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Location,Category,Tasks
from .forms import TaskImageForm
from datetime import datetime

def loginPage(request):
    if(request.user.is_authenticated):
        return redirect('home')
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request, 'User doesnt exist')

        user= authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"incorrect password")
        
    return render(request,"base/login_registration.html")

def logoutPage(request):

    logout(request)
    return redirect("home")

@login_required(login_url='loginPage')
def home(request):
    q=request.GET.get('q') if request.GET.get('q') != None else ''
    tasks = request.user.tasks_set.filter(
        location__name__icontains = q
    )
    print(tasks)
    location = Location.objects.all()
    context = {'tasks':tasks,'locations':location}
    return render(request,"base/home.html",context)

@login_required(login_url='loginPage')
def task_image(request,pk):
# room=Room.objects.get(id=pk)
    task=Tasks.objects.get(id=pk)
    if(request.user == task.assigned):
        form=TaskImageForm(instance=task)
        if request.method == "POST":
            form = TaskImageForm(request.POST,request.FILES,instance=task)
            if form.is_valid():
                temp = form.save(commit=False)
                temp.completed = datetime.now()
                temp.save()
                return HttpResponse('uploaded')
        context = {"form":form}
        return render(request,'base/task_image.html',context)
    else:
        return HttpResponse("you arent allowed here")