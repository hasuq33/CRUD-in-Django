from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from .admin import Student,Image
  
# from django.urls import reverse

# Create your views here.

def home(request):
    image = Image.objects.all()
    return render(request,'myappf/home.html',{'image': image})

def logout1(request):
    return render(request,'myappf/logout.html')

def student(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        father_name = request.POST['father name']
        mother_name = request.POST['mother name']
        address =  request.POST['address']
        gender = request.POST['gender']
        state = request.POST['state']
        city = request.POST['city']
        birth = request.POST['dob']
        enrollment = request.POST['enrollmentNo']
        course = request.POST['course']
        email = request.POST['email']


        s = Student( first_name = fname, last_name = lname, father_name = father_name, mother_name = mother_name ,  address = address, state = state,city = city ,date_of_birth = birth ,enrollment = enrollment, course = course,email=email ,gender = gender )
        s.save()
        return redirect('table')
        
    return render(request,'myappf/student_form.html')

def table(request):
    student = Student.objects.all()
    return render(request,'myappf/table.html',{'students':student})


def edit_student(request,student_id):
    student = Student.objects.get(id = student_id)
    if request.method == 'POST':
       student.enrollment =  request.POST['enrollmentNo']
       student.first_name = request.POST['fname'] 
       student.last_name =  request.POST['lname']
       student.email = request.POST['email']
       student.course = request.POST['course']
       student.save()
       return redirect('table')
    else:
        return render(request,'myappf/edit.html',{'student':student} )


def delete_student(request,student_id):
    student = Student.objects.get(id = student_id)
    student.delete()
    return redirect('table')






# This code work in User Class

def form(request):
    if request.method == 'POST':
        uname = request.POST['usrname']
        email = request.POST['email']
        psw = request.POST['psw']

        if User.objects.filter( username = uname).exists():
            messages.info(request, 'Username already exist!')
            return redirect('form')
        
        if User.objects.filter( email = email).exists():
            messages.info(request, 'email already exist')
            return redirect('form')

        
        usr = User(username = uname, email = email)
        usr.set_password(psw)
        usr.save()
        return redirect('login')

    return render(request,'myappf/index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        psw = request.POST['psw']

        if User.objects.filter(email = email).exists():
            usr = authenticate(email=email, psw=psw)

            if usr:
                login(request,usr) 
                return redirect('home')
            
            # messages.info(request,'Please insert correct password!') 
            return redirect('home')

        messages.info(request,'Please insert correct password and email!') 
        return redirect('login')

    return render(request,'myappf/login.html')

def logoutview(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('logout1')
    
    