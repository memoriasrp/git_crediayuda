from django.urls import path
from . import views as clientes_view

urlpatterns = [   
    path('<int:clientes_id>/<slug:clientes_slug>/', clientes_view.clientes, name="cliente"),
    path('<int:estadocivil_id>/<slug:estadocivil_slug>/', clientes_view.estadocivil, name="estadocivil"),
]
