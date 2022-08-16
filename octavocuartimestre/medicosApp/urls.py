from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views



from django.contrib.auth.decorators import login_required
#from .views import medicosEdit

appname ='medicosApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('registro/', views.registro, name='registro'),
    path('inicio/', views.inicio, name='inicio'),
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login_request, name='login'),
    path('condiciones/', views.condiciones, name='condiciones'),
    path('cookies/', views.cookies, name='cookies'),
    path('privacidad/', views.privacidad, name='privacidad'),
    # vista inicial admin
    path('medicos/', views.medicosHome, name='medicos'),
    path('inventarios/', views.inventarios, name='inventarios'),
    path('conferencias/', views.conferencias, name='conferencias'),
    path('consultas/', views.consultas, name='consultas'),
    #registros
    #path('regInventario/', views.inventarioFormProcess, name='regInventario'),
    # eliminaciones
    path('delConsulta/<int:id_consulta>', views.elimConsulta, name='delConsulta'),
    path('delMedico/<int:id_medico>', views.elimMedico, name='delMedico'),
    path('delInventario/<int:id_inventario>', views.elimInventario, name='delInventario'),
    path('delConferencia/<int:id_conferencia>', views.elimConferencia, name='delConferencia'),
    # updates
    path('upinventario/<int:id_inventario>', views.actualizarViewInventario, name='upInventario'),
    path('upmedico/<int:id_medico>', views.actualizarViewMedico, name='upMedico'),
    path('upconferencia/<int:id_conferencia>', views.actualizarViewConferencia, name='upConferencia'),  
    path('upconsulta/<int:id_consulta>', views.actualizarViewConsulta, name='upConsulta'),
    # mapa del sitio
    path('mapa/', views.mapa, name='mapa'),
    path('nosotros/', views.nosotros, name='nostros'),
    path('contacto/', views.contacto, name='contacto'),
]