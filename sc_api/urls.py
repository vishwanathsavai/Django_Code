# sc_api/urls.py
from django.urls import include, path
from rest_framework import routers
from django.conf.urls import url
from . import views
from . import supervisor_views
import Django_Script

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sc/login',views.login),
    path('sc/forgot',views.forgot_password),
    path('sc/otpValid',views.validate_OTP),
    path('sc/newPwd',views.New_Password),
    path('sc/signup',views.Signup),
    path('sc/signupInit',views.SignupInit),
    path('sc/sup/login',supervisor_views.Sup_Login),
    path('sc/sup/forgot',supervisor_views.Sup_forgot_password),
    path('sc/sup/otp',supervisor_views.Sup_validate_OTP),
    path('sc/sup/pwd',supervisor_views.Sup_New_Password)
]
