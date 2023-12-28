from django.urls import path
from . import views
app_name = "store_app"
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('formpage/', views.user_profile, name='formpage'),

]
