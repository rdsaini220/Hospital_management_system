from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from .models import Doctor,Patient,Appointment

# Create your views here.
def Index(request):
    return render(request,'index.html')

def Contact(request):
    return render(request,'contact.html')

def Login(request):
    error=""
    if request.method=='POST':
        uname = request.POST['uname']
        password = request.POST['pass']
        user = authenticate(username=uname,password=password)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error= "yes"
    d= {'error':error}
    return render(request,'login.html',d)



def Dashbord(request):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.all()
    patient= Patient.objects.all()
    appoint = Appointment.objects.all()
    d = len(doctor)
    p = len(patient)
    a = len(appoint)
    d_list = {"d":d,"p":p,"a":a} 
    return render(request, 'dashbord.html',d_list)

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return render(request,'index.html')

def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all().order_by('-id')
    d_list = {'doc':doc}
    return render(request,'view_doctor.html',d_list)

def Add_Doctor(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=='POST':
        dname = request.POST['name']
        dmobile = request.POST['mobile']
        dspacial = request.POST['spacial']
        try:
            Doctor.objects.create(name=dname,mobile=dmobile,spacial=dspacial)
            error="no"
        except:
            error= "yes"
    d= {'error':error}
    return render(request,'add_doctor.html',d)

def Delect_Doctor(request,id):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id=id)
    doctor.delete()
    return redirect('view_doctor')


def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pat = Patient.objects.all().order_by('-id')
    p_list = {'pat':pat}
    return render(request,'view_patient.html',p_list)

def Add_Patient(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=='POST':
        pname = request.POST['name']
        pgender = request.POST['gender']
        pmobile = request.POST['mobile']
        paddress = request.POST['address']
        try:
            Patient.objects.create(name=pname,gender=pgender,mobile=pmobile,address=paddress)
            error="no"
        except:
            error= "yes"
    d= {'error':error}
    return render(request,'add_patient.html',d)


def Delect_Patient(request,id):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=id)
    patient.delete()
    return redirect('view_patient')


def View_Appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    appoint = Appointment.objects.all().order_by('-id')
    a_list = {'appoint':appoint}
    return render(request,'view_appointment.html',a_list)

def Add_Appointment(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    pat = Patient.objects.all()
    if request.method=='POST':
        dname = request.POST['doctor']
        pname = request.POST['patient']
        date = request.POST['date']
        time = request.POST['time']
        doctor = Doctor.objects.filter(name=dname).first()
        patient = Patient.objects.filter(name=pname).first()
        try:
            Appointment.objects.create(doctor=doctor,patient=patient,date=date,time=time)
            error="no"
        except:
            error = "yes"
    d = {"doc":doc,"pat":pat,"error":error}
    return render(request,'add_appointment.html',d)


def Delect_Appointment(request,id):
    if not request.user.is_staff:
        return redirect('login')
    appoint = Appointment.objects.get(id=id)
    appoint.delete()
    return redirect('view_appointment')