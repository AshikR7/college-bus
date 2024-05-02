
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from .forms import *
from college.settings import EMAIL_HOST_USER
from django.shortcuts import render
from .models import *
import cv2
from pytesseract import pytesseract



def index(request):

    return render(request,'index.html')


def busAttendanceMorning(request):
    tes()
    a=morning(busNo=text,morg="present")
    a.save()
    sendmailMorning()
    return redirect(index)

def busAttendanceEvening(request):
    tes()
    a=evening(busNo=text,even="present")
    a.save()
    sendmailEvening()
    return redirect(index)

def dispaly(request):
    a=morning.objects.all()
    b=evening.objects.all()
    bm=[]
    m=[]
    be=[]
    e=[]
    tm=[]
    te=[]
    for i in a:
        no=i.busNo
        bm.append(no)
        me=i.morg
        m.append(me)
        t=i.time
        tm.append(t)
    mr=zip(bm,m,tm)
    for i in b:
        no=i.busNo
        be.append(no)
        ev=i.even
        e.append(ev)
        t=i.time
        te.append(t)
    vg=zip(be,e,te)
    return  render(request,'display.html',{'morning':mr,'evening':vg})
def tes():
    camera=cv2.VideoCapture(0)
    while True:
        _,Image=camera.read()
        cv2.imshow('Text Detection',Image)
        if cv2.waitKey(0)& 0xFF==ord('s'):
            cv2.imwrite('test1.jpg',Image)
            break
    camera.release()
    cv2.destroyAllWindows()
    tesseract()

def tesseract():
    path_to_tesseract=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    Imagepath='test1.jpg'
    pytesseract.tesseract_cmd=path_to_tesseract
    global text
    text = pytesseract.image_to_string(Imagepath)
    print(text[:-1])

def busRegister(request):
    if request.method=='POST':
        bus=busForm(request.POST,request.FILES)
        a=busModel(busNo=bus)
        a.save()
        return redirect(index)
    return render(request,"busRegester.html")

def mailRegister(request):
    if request.method=='POST':
        a=mailForm(request.POST)
        if a.is_valid():
            ma=a.cleaned_data['mail']
            m=mailModel(mail=ma)
            m.save()
        return redirect(index)
    return render(request,"mail.html")

def sendmailMorning():
    a= mailModel.objects.all()
    for i in a:
        email = i.mail
        subject="College Bus"
        message=" The Bus has arrived at college"
        email_from = EMAIL_HOST_USER
        recipient = [email]
        send_mail(subject, message, email_from, recipient)

def sendmailEvening():
    a = mailModel.objects.all()
    for i in a:
        email = i.mail
        subject = "College Bus"
        message = "The Bus has departed from college"
        email_from = EMAIL_HOST_USER
        recipient = [email]
        send_mail(subject, message, email_from, recipient)



def maildis(request):
    a=mailModel.objects.all()
    m=[]
    for i in a:
        mi=i.mail
        m.append(mi)
    return  render(request,'maildisplay.html',{'mail':m})

