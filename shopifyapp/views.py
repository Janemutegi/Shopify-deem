
from itertools import product
from venv import create

from django.shortcuts import render, redirect
from django.template.context_processors import request


from shopifyapp.forms import ImageUploadForm, LoginForm
from shopifyapp.models import Subscribe, Products, VehicleReport, WebsiteContent, Register, CreateForm,LoginForms


# Create your views here.
def home(request):
    return render(request, 'home.html')

def cart(request):
    return render(request, 'cart.html')
def contact(request):
    return render(request, 'contact.html')
def checkout(request):
    return render(request, 'checkout.html')
def detail(request):
    return render(request, 'detail.html')
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
           datetime = request.POST['date']

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
            date=request.POST['date']

        )

        report_issue.save()
        return redirect('/report_success')
    else:
            return render(request, 'report_unsuccessful.html')

def search(request):
    query = request.POST['search']
    products = Products.objects.filter(name__icontains=query)
    return render(request, 'index.html', {'products': list_products})

def list_products(request):
    products= Products.objects.all()
    return render(request, 'index.html', {'products': products})





def logins(request):

        return render(request, 'login.html')


def products(request):
    return render(request, 'products.html')

def about(request):
        return render(request, 'about.html')


def create_form(request):
    if request.method == "POST":
        creates = CreateForm(
            firstname=request.POST['firstname'],
            lastname=request.POST['lastname'],
            email = request.POST['email'],
            password=request.POST['password']
        )

        creates.save()
        return redirect('/login')
    else:
        return render(request, 'creates.html')





def base(request):
    return render(request, 'base.html')


def logins_unsuccessful(request):
    return render(request, 'login_unsuccessful.html')


def login_success(request):
    return render(request, 'login_success.html')


def create_unsuccessful(request):
    return render(request, 'create_unsuccessful.html')


def shop(request):
    return render(request, 'shop.html')

def report_unsuccessful(request):
    return render(request, 'report_unsuccessful.html')

def search(request):
    return render(request, 'search.html')
def report_success(request):
    return render(request, 'report_success.html')
def register_success(request):
    return render(request, 'register_success.html')
def register_success1(request):
    return render(request, 'newsletter/register_success.html')
def report(request):
    return render(request, 'report.html')

def search_content(request):
    query = request.GET.get('q', '')
    results = []

    if query:
        results = WebsiteContent.objects.filter(
            title__icontains=query
        ) | WebsiteContent.objects.filter(
            content__icontains=query
        )

    return render(request, 'search.html', {'query': query, 'results': results})

def show_image(request):
    images = VehicleReport.objects.all()
    return render(request, 'show_image.html', {'images': images})

def imagedelete(request, id):
    image = VehicleReport.objects.get(id=id)
    image.delete()
    return redirect('/show_image')