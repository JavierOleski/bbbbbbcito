from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app import views



urlpatterns = [

    path('example/', views.example, name="example"),
    path('example/list/', views.example_list, name="example_list"),
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('acercade/', views.acercade, name="acercade"),
    path('registro/', views.registrarse, name="registro"),
    path('pacientes/', views.lista_pacientes, name="lista_pacientes"),
    path('pacientes/ficha/', views.ficha, name="ficha"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
