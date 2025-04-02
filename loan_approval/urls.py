from django.contrib import admin
from django.urls import path, include
from .import views
from .views import feedback
app_name = 'loan_approval'  # ✅ This registers the namespace



urlpatterns = [
    path("",views.home, name='home'),
   
    path("calculator/",views.calculator,name='calculator'),
    path("feedback/",views.feedback, name='feedback'),
    # path('feedback/', feedback, name='feedback'),
    path("home-loan/",views.home_loan),
    path("home-loan-form/",views.home_form,name='home-loan-form'),
    path("personal-loan/",views.persona_loan,name='personal-loan-form'),
    path("personal-loan-form/",views.personal_loan_form,name='personal-loan-form'),
    path("gold-loan-form/result/",views.gold_result,name='gold-loan-form-result'),
    path("home-loan-form/result/",views.home_result,name="home-loan-form-result"),
    path("personal-loan-form/result/",views.personal_result,name="personal-loan-form-result"),
    path("gold-loan-form/",views.gold_form,name='gold-loan-form'),
    path("privacy-policy/",views.privacy_policy,name='privacy-policy'),
    path("about-us/",views.about_us,name='about-us'),
    

]

