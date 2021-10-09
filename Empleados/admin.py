from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import *

# crear un formulario basado en el modelo sobreescrito de User
class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


# Sobreescribir la clase UserAdmin para mostrar el formulario recien creado 'MyUserChangeForm'
# toca agregar los campos nuevos
class UserAdmin(UserAdmin):
    form = MyUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': (
                'tipo_id',
                'num_documento',
                'genero',
                'fecha_nacimiento',
                'dependencia',
                'cargo',
                'tipo_contrato',
                'fecha_inicio_contrato',
                'fecha_fin_contrato',
                'salario',
            )}),
    )

admin.site.register(User,UserAdmin)
admin.site.register(prueba)