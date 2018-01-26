from django.shortcuts import render
import random
from models import Student
def new(request):
    num = random.randint(3,11)
    context = {
        'num': num
    }
    return render(request, 'houses/new.html',context)
def create(request):
    print "you try create a wand"
    peep = request.POST['name']
    request.session['peep'] = peep
    students = Student.objects.all()
    context= {
        'peeps': students
    }
    return render(request,'houses/index.html', context)
def show(request, info):
    print info
    return
