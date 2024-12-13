
from itertools import product
from venv import create

from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.utils import timezone

from shopifyapp.forms import LoginForm
from shopifyapp.models import Subscribe, VehicleReport, Register,LoginForms


# Create your views here.
def home(request):
    return render(request, 'home.html')

#def cart(request):
    #return render(request, 'cart.html')
def contact(request):
    return render(request, 'contact.html')
#def checkout(request):
    #return render(request, 'checkout.html')
#def detail(request):
   # return render(request, 'detail.html')

def migration_reset(request):
    return render(request, 'migration_reset.html')

def index(request):
   if request.method == "POST":
       member = Subscribe(
           email = request.POST['email'],

       )
       member.save()
       return redirect('/')
   else:
       return render(request, 'index.html')

def registers(request):
   if request.method == "POST":
       register = Register(
           name = request.POST['name'],
           email = request.POST['email'],
           phone = request.POST['phone'],
           date=timezone.now()

       )
       register.save()
       return redirect('/register_success')
   else:
       return render(request, 'newsletter.html')


def report_issues(request):
    if request.method == "POST":
        report_issue = VehicleReport(
            customer_name=request.POST['customer_name'],
            phone=request.POST['phone'],
            description=request.POST['description'],
            vehicle_image=request.POST['images'],
            datetime=timezone.now()

        )

        report_issue.save()
        return redirect('/report_success')
    else:
            return render(request, 'report_unsuccessful.html')





def logins(request):

        return render(request, 'login.html')

def about(request):
        return render(request, 'about.html')




def base(request):
    return render(request, 'base.html')


def logins_unsuccessful(request):
    return render(request, 'login_unsuccessful.html')


def login_success(request):
    return render(request, 'login_success.html')


#def create_unsuccessful(request):
    #return render(request, 'create_unsuccessful.html')


#def shop(request):
   # return render(request, 'shop.html')

def report_unsuccessful(request):
    return render(request, 'report_unsuccessful.html')

#def search(request):
   # return render(request, 'search.html')
def report_success(request):
    return render(request, 'report_success.html')
def register_success(request):
    return render(request, 'register_success.html')
def register_success1(request):
    return render(request, 'newsletter/register_success.html')
def report(request):
    return render(request, 'report.html')
