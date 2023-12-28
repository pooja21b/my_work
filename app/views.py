import random
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse
from .models import Tblone, Tbltwo, Tblthree


# Create your views here.
def register(request):
    if request.method == 'POST':
       firstname=request.POST.get('uname')
       username=request.POST.get('fname')
       lastname=request.POST.get('lname')
       email=request.POST.get('mail')
       password=request.POST.get('pwd')
       retypepassword=request.POST.get('retypepassword')
       if password != retypepassword:
           messages.error("Your password and confrim password are not same!!")
       else:
           my_user=Tblone.objects.create(uname=username,fname=firstname,lname=lastname,mail=email,pwd=password)
           my_user.save()
           return redirect('/app/login/')
    return render(request, 'register.html')

def handlelogin(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render({}, request))

def loginsubmit(request):
   if request.method == 'POST':
       mail=request.POST.get('mail')
       pwd=request.POST.get('pwd')
       myuser=Tblone.objects.filter(mail=mail,pwd=pwd).count()
       if myuser > 0:
            request.session['smail']=mail
            User= Tblone.objects.filter(mail=mail,pwd=pwd).first()
            #print('dgfdv sefgrf   edsfsd'+User)
            #Tblone.objects.filter(mail=mail,pwd=pwd).first()
            request.session['UserID']=User.id
            return redirect('home')
       else:
            messages.error("Invalid credentials Please Try Again...!!! ")
            return redirect('login')

def home(request):
    smail = request.session['smail']
    if len(smail) > 0:
        return render(request,'home.html')
    else:
        return redirect('login')
def projectview(request):
   if  request.session['UserID']!=None:
    smail = request.session['smail']
    if len(smail) > 0:

     pro = Tbltwo.objects.all().values()
     template = loader.get_template('projectview.html')
     list = [random.randint(1, 5)]
     context = {'proj': pro, 'v1': list}
     return HttpResponse(template.render(context, request))
   else:
    return redirect('login')


def logout(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request,'Successfully Logged out')
        return redirect('/app/login')
    return render(request, 'logout.html')

def myaccount(request):

    return render(request,'myaccount.html')

def accountdetails(request):
    template = loader.get_template('accountdetails.html')
    return HttpResponse(template.render({}, request))

def update_details(request):
    pass

def yourmembership(request):
    return render (request,'yourmembership.html')

def changepassword(request):
    template = loader.get_template('changepassword.html')
    return HttpResponse(template.render({}, request))

def changepasswordbtn(request):
    if request.session['UserID'] is not None:
        smail = request.session['smail']
        print(smail)
        if len(smail) > 0:
            if request.method == "POST":
                ID = request.session['UserID']

                if 'pm' in request.POST:
                    pm = request.POST['pm']
                else:
                    pm = False

                if 'p1' in request.POST:
                    p1 = request.POST['p1']
                else:
                    p1 = False

                if 'p2' in request.POST:
                    p2 = request.POST['p2']
                else:
                    p2 = False

                if 'p3' in request.POST:
                    p3 = request.POST['p3']
                else:
                    p3 = False

                if p1 and p2:
                    user = Tblone.objects.get(id=ID)
                    if user.pwd == p1:
                        user.pwd = p2
                        if p2 != p3:
                            messages.error(request, 'Password And RetypePassword Not Same...!!!')
                        else:
                           user.save()
                           messages.success(request, 'Your Password Is Successfully Changed....!!!')
                           return redirect('login')

                    else:
                          messages.error(request, "Previous Password Does Not Match...!!!")
                else:
                           messages.error(request, "Missing password...!!! ")

            return render(request, 'changepassword.html')


def Invoices(request):
    return render (request,'Invoices.html')

def FAQ(request):
    return render (request,'FAQ.html')

def settings(request):
    return render (request,'settings.html')

def handlecrawling(request):
    if request.session['UserID'] != None:
        smail = request.session['smail']
        if len(smail) > 0:
           crwl = Tblthree.objects.all().values()
           template = loader.get_template('crawling.html')
           context = {'crawl': crwl}
           return HttpResponse(template.render(context, request))
        else:
           return redirect('login')

def dashboard(request):
    if request.session['UserID'] != None:
        smail = request.session['smail']
        if len(smail) > 0:
          dash = Tblthree.objects.all().values()
          template = loader.get_template('dashboard.html')
          context = {'board': dash}
          return HttpResponse(template.render(context, request))
        else:
           return redirect('login')


def add(request):
    template = loader.get_template('addproject.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    w= request.POST['url']
    x = request.POST['pname']
    pro = Tbltwo(url=w, pname=x)
    pro.save()
    return redirect('/app/projectview')

def delete(request,id):
    pro = Tbltwo.objects.get(id=id)
    pro.delete()
    return HttpResponseRedirect(reverse('/app/projectview'))

def edit (request,id):
    pro = Tbltwo.objects.get(id=id)
    template = loader.get_template('editproject.html')
    context = {'proj': pro}
    return HttpResponse(template.render(context, request))


def editrecord(request,id):
    c = request.POST['pname']
    d = request.POST['url']
    Project = Tbltwo.objects.get(id=id)
    Project.pname = c
    Project.url = d
    Project.save()
    return redirect('/app/projectview')


