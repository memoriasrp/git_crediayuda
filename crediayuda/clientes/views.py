from django.shortcuts import render, get_object_or_404
from .models import Clientes, EstadoCivil, TipoDireccion, TipoTelefono, Banco

# Create your views here.
def clientes(request, clientes_id, clientes_slug):
    clientes= get_object_or_404(Clientes, id=clientes_id)
    return render(request, 'clientes/sample.html', {'clientes':clientes})

def estadocivil(request, estadocivil_id, estadocivil_slug):
    clientes= get_object_or_404(EstadoCivil, id=estadocivil_id)
    return render(request, 'clientes/sample.html', {'estadocivil':estadocivil})

