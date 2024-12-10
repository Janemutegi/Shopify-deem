
from django.contrib import admin
from django.urls import path
from shopifyapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='subscribe'),
    path('home/', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
    path('contact/', views.contact, name='contact'),
    path('checkout/', views.checkout, name='checkout'),
    path('detail/', views.detail, name='detail'),
    path('shop/', views.shop, name='shop'),
    path('newsletter/', views.registers, name='newsletter'),
    path('search/', views.search, name='search'),
    path('base/', views.base, name='base'),
    path('', views.logins, name='login'),
    path('products/', views.products, name='products'),
    path('about/', views.about, name='about'),
    path('login/login_success/', views.login_success, name='login_success'),

    path('creates/', views.create_form, name='creates'),

    path('create_unsuccessful/', views.create_unsuccessful, name='create_unsuccessful'),

    path('report/', views.report, name='report'),

    path('report/report_success/', views.report_success, name='report_success'),
    path('report/report_unsuccessful/', views.report_unsuccessful, name='report_unsuccessful'),

    path('register_success/', views.register_success, name='register_success'),





    path('showimage/', views.show_image, name='image'),
    path('imagedelete/<int:id>', views.imagedelete),

  #  path('pay/', views.pay, name='pay'),
   # path('stk/', views.stk, name='stk'),
    #path('token/', views.token, name='token'),
]
