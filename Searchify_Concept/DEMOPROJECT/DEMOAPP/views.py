from django.shortcuts import render
import mysql.connector as db
import pandas as pd
F_N=''
L_N=''
EMAIL=''
P_N=''
MSSG=''
TOP=''
confirm=''
password=''
username=''
# Create your views here.

def Contactinfo(request):
    global F_N,L_N,EMAIL,P_N,MSSG
    if request.method=='POST':
        mysql=db.connect(host='localhost',user='root',password='Giratina@0123',database='project')
        cursor=mysql.cursor()
        d=request.POST
        for key,value in d.items():
            if key=='fname':
                F_N=value
            if key=='lname':
                L_N=value
            if key=='contactEmail':
                EMAIL=value
            if key=='contactPhone':
                P_N=value
            if key=='comment':
                MSSG=value

        c="insert into info_people values('{}','{}','{}','{}','{}')".format(F_N,L_N,EMAIL,P_N,MSSG)
        cursor.execute(c)
        mysql.commit()
    return render(request,'DEMOAPP/Contact.html')
    
def AboutUs(request):
    return render(request,'DEMOAPP/AboutUs.html')
def TEAM(request):
    return render(request,'DEMOAPP/Team.html')
def HOME(request):
    return render(request,'DEMOAPP/Home.html')
def SUPPORT(request):

    return render(request,'DEMOAPP/SUPPORT.html')
def Maintanace(request):

    return render(request,'DEMOAPP/Maintanace.html')

def signup(request):
    global EMAIL,P_N,C_N
    if request.method=='POST':
        mysql=db.connect(host='localhost',user='root',password='Giratina@0123',database='project')
        cursor=mysql.cursor()
        d=request.POST
        for key,value in d.items():
            if key=='email':
                username=value
            if key=='psw':
                password=value
            if key=='psw-repeat':
                confirm=value
        c="insert into signup values('{}','{}','{}')".format(username,password,confirm)
        cursor.execute(c)
        mysql.commit()
    return render(request,'DEMOAPP/signup.html')
def team(request):

    return render(request,'DEMOAPP/team.html')