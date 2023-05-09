from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tecnica/', views.tecnica, name='tecnica'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('galeria/', views.galeria, name='galeria'),
    path('contacto/', views.contacto, name='contacto'),
    path('prod_detalle/<str:id>/', views.prod_detalle, name='prod_detalle'),
]
