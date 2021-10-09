from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    cedula = 'Cedula'
    ti = 'Tarjeta de Identidad'
    passport = 'Pasaporte'
    nit = 'Nit'
    tip_id = [
        (cedula, 'Cedula'),
        (ti, 'Tarjeta de Identidad'),
        (passport, 'Pasaporte'),
        (nit, 'Nit'),
    ]

    masculino = 'Masculino'
    femenino = 'Femenino'
    gener = [
        (masculino, 'Masculino'),
        (femenino, 'Femenino'),
    ]

    indefinido = 'Indefinido'
    Fijo = 'Termino Fijo'
    ops = 'Prestacion de Servicios'
    obra_labor = 'Obra Labor'
    tip_contrato = [    
        (indefinido , 'Indefinido'),
        (Fijo , 'Termino Fijo'),
        (ops , 'Prestacion de Servicios'),
        (obra_labor , 'Obra Labor'),
    ]
    tipo_id = models.CharField('Tipo Identificacion',max_length = 25, choices = tip_id, default = cedula)
    num_documento = models.CharField('Número de Documento',max_length=15, null = True, blank = False)
    genero = models.CharField('Genero',max_length = 9, choices = gener, default = masculino)
    fecha_nacimiento = models.DateField('Fecha de Nacimiento', null = True)
    dependencia = models.CharField('Dependencia', max_length = 70, null = True, blank = False)
    cargo = models.CharField('Cargo',max_length = 50, null = True, blank = False)
    tipo_contrato = models.CharField('Tipo de Contrato',choices = tip_contrato, max_length = 23, default = indefinido, blank = False )
    fecha_inicio_contrato = models.DateField('Fecha Inicio de Contrato',null = True)
    fecha_fin_contrato = models.DateField('Fecha Fin de Contrato',null = True)
    salario = models.FloatField('Salario',null = True)

class prueba(models.Model):
    num_document = models.CharField('Número de Documento',max_length=15, null = True, blank = False)
