from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name="main"),
    path('service/', views.service_page, name="service"),
    path('contacts/', views.about_page, name="reg"),
    path('list/', views.list_page, name="list"),
    path('<int:id>/', views.list_page_delete, name="list_delete"),
    path('<slug:slug>/', views.training_page, name="training"),
    
]