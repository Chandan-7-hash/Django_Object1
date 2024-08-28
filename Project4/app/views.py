from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    rollno = '2'
    name = 'Bill'
    pno ='+91 8869187688'
    email = 'Bill@gmail.com'
    cls = '12'
    st = Student(rollno=rollno, name=name, pno=pno, email=email, cls=cls)
    
    user = {'rollno': rollno, 'name':name, 'pno': pno, 'email': email, 'cls': cls}
    return render(request, 'index.html', user)