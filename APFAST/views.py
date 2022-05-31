from django.http import HttpResponse
from django.shortcuts import render, redirect

def hello(request): 
    return HttpResponse('Hello World')


# def index(request):
#     return render(request, 'hello.html',{'name' : "Mosh"})


# def room(request):
#     rooms = Room.objects.all()
#     return render(request, 'home.html', {'rooms' : rooms})
 

# def deleteRoom(request,pk):
#     selectedRoom = Room.objects.get(id=pk)
#     selectedRoom.delete()
#     return redirect('../')