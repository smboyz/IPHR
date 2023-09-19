from django.contrib import admin
from django.urls import path
from iphr import views
from .views import *

urlpatterns = [
    path("",const,name="const"),
    path("home", views.Base, name="home"),
    path("service/<int:id>/", views.service, name="service"),
    path("contact",views.contact, name="contact"),
    path("mass",mass, name="mass"),
    path("staffing",staffing, name="staffing"),
    path("recruiment",views.recruiment, name="recruiment"),
    path("submit_cv",submit_cv, name="submit_cv"),
    path("all_job",all_job, name="all_job"),
    path("about",about, name="about"),
    path("oli_gas",oli_gas, name="oli_gas"),
    path("ecommerce",ecommerce, name="ecommerce"),
    path("manufacturing",manufacturing, name="manufacturing"),
    path("hospitality",hospitality, name="hospitality"),
    path("healthcare",healthcare, name="healthcare"),
    path("financial",financial, name="financial"),
    path("hr_business",hr_business, name="hr_business"),
    path("realestate",realestate, name="realestate"),
    path("supplychain",supplychain, name="supplychain"),
    path("energychemical",energychemical, name="energychemical"),
    path("retailtrading",retailtrading, name="retailtrading"),
    path("fmcg",fmcg, name="fmcg"),
    path("shipping",shipping, name="shipping"),
    path("information",information, name="information"),
    path("menu/<str:name>/",views.redirect_to_url , name="menu"),
    path("submenu/<str:name>/", views.redirect_to_url, name="submenu"),
    

]
