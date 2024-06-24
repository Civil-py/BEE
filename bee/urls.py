from django.urls import path
from . import views


urlpatterns = [
    path("home", views.index, name="index"),
path("", views.landingpage, name="landingpage"),
path("register", views.register, name="register"),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

path("Inputs/<str:choice>", views.inputs, name="inputs"),
path("Financial-Inputs/<str:choice>", views.financial_inputs, name="financial_inputs"),
]