from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class EstadoCivil(models.Model):
    descripcion = models.CharField(verbose_name="estado Civil", max_length=20)
    class Meta:
        verbose_name = "Estado Civil"
        verbose_name_plural = "Estado Civil"
    
    def __str__(self):
        return  self.descripcion

class Banco(models.Model):
    descripcion=models.CharField(verbose_name="entidad Bancaria", max_length=50)
    class Meta:
        verbose_name = "Entidad Bancaria"
        verbose_name_plural = "Entidades Bancarias"
    
    def __str__(self):
        return  self.descripcion

class CompaniaCel(models.Model):
    descripcion=models.CharField(verbose_name="entidad Bancaria", max_length=50)
    class Meta:
        verbose_name = "Red Telefonica"
        verbose_name_plural = "Redes Telefonicas"
    def __str__(self):
        return  self.descripcion

class TipoDireccion(models.Model):
    descripcion =models.CharField(verbose_name="Tipo de direccion", max_length=50)
    class Meta:
        verbose_name = "Tipo de direccion"
        verbose_name_plural = "Tipos de direccion"

    def __str__(self):
        return  self.descripcion

class TipoTelefono(models.Model):
    descripcion =models.CharField(verbose_name="Tipo de telefono", max_length=50)
    class Meta:
        verbose_name = "Tipo de Telefono"
        verbose_name_plural = "Tipos de Telefono"

    def __str__(self):
        return  self.descripcion

class Clientes(models.Model):       
    dni= models.CharField(verbose_name="DNI", max_length=12, unique=True)
    nombre =models.CharField(verbose_name="nombre", max_length=100)
    apellidos  =models.CharField(verbose_name="Apellidos", max_length=100)
    estado_civil = models.ForeignKey(EstadoCivil, on_delete =models.CASCADE)
    conyugue = models.CharField(verbose_name="conyugue", max_length=100 , null=True, blank=True)
    dni_conyugue= models.CharField(verbose_name="DNI Conyugue", max_length=12 , null=True, blank=True)
    correo = models.EmailField(verbose_name="email", max_length=100 , null=True, blank=True)
    centro_laboral = models.CharField(verbose_name="centro_laboral", max_length=50 , null=True, blank=True)
    banco= models.ForeignKey(Banco, on_delete =models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")


    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"
        ordering = ['apellidos', 'nombre']

    def __str__(self):
        return "("+self.dni+")-" + self.apellidos + ", "+self.nombre

class Cliente_telefono(models.Model):
    numero = models.CharField(verbose_name="numero Telefono", max_length=12)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    tipo_numero=models.ForeignKey(TipoTelefono, on_delete=models.CASCADE )
    orden = models.IntegerField(blank=True, null=True, default=0)


class Cliente_direccion(models.Model):
    numero = models.CharField(verbose_name="numero direccion", max_length=12)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    tipo_direccion=models.ForeignKey(TipoDireccion, on_delete=models.CASCADE )
    orden = models.IntegerField(blank=True, null=True, default=0)
