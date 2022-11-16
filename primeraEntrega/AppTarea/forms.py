from django import forms

class CrearCurso(forms.Form):
    
    nombre = forms.CharField()
    comision = forms.IntegerField()

class CrearAula(forms.Form):
    materia = forms.CharField(max_length=40)
    numero = forms.IntegerField()
    tamaño = forms.IntegerField()


class CrearEdificio(forms.Form):
    pisos = forms.IntegerField()
    facultad = forms.CharField(max_length=40)
    cantidad_de_aulas = forms.IntegerField()