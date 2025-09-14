from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('payment/', views.payment,name='payment'),
    path('otp/',views.otp,name='otp'),
    path('send_sms/',views.send_sms,name='send_sms'),
    path('login/', views.login,name='login'),
    path('confirm/', views.confirm,name='confirm'),
    path('passi/', views.passi,name='passi'),

]