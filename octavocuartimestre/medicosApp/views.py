import logging
logger = logging.getLogger(__name__)
from telnetlib import LOGOUT
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import medicosForm, consultaForm, inventarioForm, conferenciaForm
from .models import medico, inventario, conferencia, consulta

#registros
def inventarios(request):
    inventarioFormulario = inventarioForm()
    inventarioValues = inventario.objects.all()
    if request.method == 'POST':
        form = inventarioForm(request.POST)
        if form.is_valid():
            inventarios = inventario()
            inventarios.id_inventario = form.cleaned_data.get('id_inventario')
            inventarios.nombreMat = form.cleaned_data.get('nombreMat')
            inventarios.tipo = form.cleaned_data.get('tipo')
            inventarios.cantidad = form.cleaned_data.get('cantidad')
            inventarios.save()
            messages.success(request, f'Material registrado correctamente ' + inventarios.nombreMat)
            logger.debug('registro de inventario ' + inventarios.nombreMat)
        else:
            messages.error(request, "Error al crear inventario")
            logger.debug('Error al crear inventario')

    return render(
        request, 'crud/inventario.html', {
            'inventarioValues': inventarioValues,
            'formInventario': inventarioFormulario
        })

def conferencias(request):
    conferenciaFormulario = conferenciaForm()
    conferenciasValues = conferencia.objects.all()
    if request.method == 'POST':
        form = conferenciaForm(request.POST)
        if form.is_valid():
            conferencias = conferencia()
            conferencias.id_conferencia = form.cleaned_data.get(
                'id_conferencia')
            conferencias.tema = form.cleaned_data.get('tema')
            conferencias.grupo = form.cleaned_data.get('grupo')
            conferencias.fecha = form.cleaned_data.get('fecha')
            conferencias.save()
            messages.success(request, f'Conferencia registrada correctamente ' + conferencias.tema)
            logger.debug('registro en conferencia ' + conferencias.tema)
        else:
            messages.error(request, "Error al crear conferencia")
            logger.debug('Error al crear conferencia')
    return render(
        request, 'crud/conferencias.html', {
            'conferenciasValues': conferenciasValues,
            'formConferencia': conferenciaFormulario
        })

def consultas(request):
    consultaFormulario = consultaForm()
    consultaValues = consulta.objects.all()
    if request.method == 'POST':
        form = consultaForm(request.POST)
        if form.is_valid():
            consultas = consulta()
            consultas.id_consulta = form.cleaned_data.get('id_consulta')
            consultas.fechaConsulta = form.cleaned_data.get('fechaConsulta')
            consultas.nombrePaci = form.cleaned_data.get('nombrePaci')
            consultas.apPatPaci = form.cleaned_data.get('apPatPaci')
            consultas.apMatPaci = form.cleaned_data.get('apMatPaci')
            consultas.edadPaci = form.cleaned_data.get('edadPaci')
            consultas.sexoPaci = form.cleaned_data.get('sexoPaci')
            consultas.tipoPaci = form.cleaned_data.get('tipoPaci')
            consultas.motivoCons = form.cleaned_data.get('motivoCons')
            consultas.solucion = form.cleaned_data.get('solucion')
            consultas.save()
            messages.success(request, f'Consulta registrada correctamente')
            logger.debug('Registro de consulta ' + consultas.nombrePaci)
        else:
            messages.error(request, "Error al crear consulta")
            logger.debug('Error al crear consulta')
    return render(request, 'crud/consultas.html', {
        'consultaValues': consultaValues,
        'formConsulta': consultaFormulario
    })

def medicosHome(request):
    medicosFormulario = medicosForm()
    medicosValues = medico.objects.all()
    if request.method == 'POST':
        form = medicosForm(request.POST)
        if form.is_valid():
            medicos = medico()
            medicos.id_medico = form.cleaned_data.get('id_medico')
            medicos.nomMed = form.cleaned_data.get('nomMed')
            medicos.aPat = form.cleaned_data.get('aPat')
            medicos.aMat = form.cleaned_data.get('aMat')
            medicos.edad = form.cleaned_data.get('edad')
            medicos.sexo = form.cleaned_data.get('sexo')
            medicos.save()
            messages.success(request, f'Medico registrada correctamente ' + medicos.nomMed)
            logger.debug('Registro de medico ' + medicos.nomMed)
        else:
            messages.error(request, "Error al crear medico")
            logger.debug('Error al crear medico')
    return render(request, 'crud/medicos.html', {
        "medicosValues": medicosValues,
        "formMed": medicosFormulario
    })

#Actualizaciones
def actualizarViewInventario(request, id_inventario):
        inventValue = inventario.objects.filter(pk=id_inventario).first()
        formInvent = inventarioForm(instance=inventValue)

        if request.method == 'POST':
            form = inventarioForm(request.POST, instance=inventValue)
            if form.is_valid():
                form.save()
                messages.success(request, f'Inventario actualizado correctamente ' + inventValue.nombreMat)
                logger.debug('Actualizacion de inventario ' + inventValue.nombreMat)
                return redirect('inventarios')
            else:
                messages.error(request, "Error al actualizar inventario")
                logger.debug('Error al actualizar inventario')

        return render(request, 'crud/inventarioUp.html', {'formInvent': formInvent})

def actualizarViewMedico(request, id_medico):
        medValue = medico.objects.filter(pk=id_medico).first()
        formMed = medicosForm(instance=medValue)

        if request.method == 'POST':
            form = medicosForm(request.POST, instance=medValue)
            if form.is_valid():
                form.save()
                messages.success(request, f'Medico actualizado correctamente ' + medValue.nomMed)
                logger.debug('Actualizacion de medico ' + medValue.nomMed)
                return redirect('medicos')
            else:
                messages.error(request, "Error al actualizar medico")
                logger.debug('Error al actualizar medico')

        return render(request, 'crud/medicosUp.html', {'formMed': formMed})

def actualizarViewConferencia(request, id_conferencia):
        confValue = conferencia.objects.filter(pk=id_conferencia).first()
        formConf = conferenciaForm(instance=confValue)

        if request.method == 'POST':
            form = conferenciaForm(request.POST, instance=confValue)
            if form.is_valid():
                form.save()
                messages.success(request, f'Conferencia actualizado correctamente ' + confValue.tema)
                logger.debug('Actualizacion de conferencia ' + confValue.tema)
                return redirect('conferencias')
            else:
                messages.error(request, "Error al actualizar conferencia")
                logging.debug('Error al actualizar conferencia')

        return render(request, 'crud/conferenciasUp.html', {'formConf': formConf})

def actualizarViewConsulta(request, id_consulta):
        consValue = consulta.objects.filter(pk=id_consulta).first()
        formCons = consultaForm(instance=consValue)

        if request.method == 'POST':
            form = consultaForm(request.POST, instance=consValue)
            if form.is_valid():
                form.save()
                messages.success(request, f'Consulta actualizado correctamente ' + consValue.nombrePaci)
                logger.debug('Actualizacion de consulta ' + consValue.nombrePaci)
                return redirect('consultas')
            else:
                messages.error(request, "Error al actualizar consulta")
                logging.debug('Error al actualizar consulta')

        return render(request, 'crud/consultasUp.html', {'formCons': formCons})

# Create your views here.
def home(request):
    return render(request, 'home.html')

def inicio(request):
    return render(request, 'inicio.html')

def condiciones(request):
    return render(request, 'condiciones.html')

def cookies(request):
    return render(request, 'cookies.html')

def privacidad(request):
    return render(request, 'privacidad.html')

def mapa(request):
    return render(request, 'mapa.html')

def contacto(request):
    return render(request, 'contacto.html')

def nosotros(request):
    return render(request, 'nosotros.html')
    

#Registro de un usuario para el sistema
def registro(request):
    form = UserCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            usuario = form.save()
            nombreUsuario = form.cleaned_data.get('username')
            messages.success(
                request, f'Usuario creado correctamente : {nombreUsuario}')
            messages.success(request,
                             f'Iniciaste sesion como: {nombreUsuario}')
            logger.debug('Registro de usuario ' + nombreUsuario)
            login(request, usuario)
            return redirect('inicio')
    else:
        for msg in form.error_messages:
            messages.error(request, f'error en {msg}: {form.error_messages[msg]}')
            logger.debug('Error al crear usuario')
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

#cierre de sesion  con el usuario 
def logout_request(request):
    logout(request)
    messages.info(request, "Saliste exitosamente! " + request.user.username)
    logger.debug('Cierre de sesion de usuario ' + request.user.username)
    return redirect("home")

#Inicio de sesion con usuarios en BD
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Iniciaste sesion como: {usuario}')
                logger.debug('Inicio de sesion de usuario: ' + usuario)
                return redirect('inicio')
            else:
                messages.error(request, "Usuario o contraseña incorrectos")
                logger.debug('fallo de sesion de usuario: ' + usuario)
        else:
            messages.error(request, "Usuario o contraseña incorrectos")
            logger.debug('fallo de sesion de usuario')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

#Eliminaciones
def elimConsulta(request, id_consulta):
    consultaValues = consulta.objects.get(id_consulta=id_consulta)
    consultaValues.delete()
    messages.warning(request, f'Consulta eliminada correctamente ' + consultaValues.nombrePaci)
    logger.debug('Eliminacion de consulta ' + str(id_consulta))
    return redirect('consultas')

def elimMedico(request, id_medico):
    medicoValue = medico.objects.get(id_medico=id_medico)
    medicoValue.delete()
    messages.warning(request, f'Medico eliminado correctamente ' + medicoValue.nomMed)
    logger.debug('Eliminacion de medico ' + medicoValue.nomMed)
    return redirect('medicos')

def elimConferencia(request, id_conferencia):
    conferenciaValue = conferencia.objects.get(id_conferencia=id_conferencia)
    conferenciaValue.delete()
    messages.warning(request, f'Conferencia eliminada correctamente ' + conferenciaValue.tema)
    logger.debug('Eliminacion de conferencia ' + conferenciaValue.tema)
    return redirect('conferencias')

def elimInventario(request, id_inventario):
    inventarioValue = inventario.objects.get(id_inventario=id_inventario)
    inventarioValue.delete()
    messages.warning(request, f'Inventario eliminado correctamente ' + inventarioValue.nombre)
    logger.debug('Eliminacion de inventario ' + inventarioValue.nombre) 
    return redirect('inventarios')
