from django.urls import path
from . import views


urlpatterns = [
    path("home", views.index, name="index"),
path("", views.landingpage, name="landingpage"),
path("register", views.register, name="register"),


    path('cognito/callback/', views.cognito_callback, name='cognito_callback'),
path('user-info/<str:username>/', views.get_cognito_user_info, name='user-info'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

path("home/Inputs/<str:choice>", views.inputs, name="inputs"),
path("Financial-Inputs/<str:choice>", views.financial_inputs, name="financial_inputs"),
]
