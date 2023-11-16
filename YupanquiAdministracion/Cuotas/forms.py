from django import forms
from .models import CuotaMensual, CuotaActividad
import datetime


class CuotaMensualForm(forms.ModelForm):
    class Meta:
        model = CuotaMensual
        fields = [ 'socio', 'mes', 'ano','monto', 'fecha_pago']

        def clean(self):
            cleaned_data = super().clean()
            mes = cleaned_data.get('mes')
            ano = cleaned_data.get('ano')
            socio = cleaned_data.get('socio')

        # Verifica si ya existe una cuota registrada para el mismo mes y año
            cuota_existente = CuotaMensual.objects.filter(socio=socio, mes=mes, ano=ano).exists()

            if cuota_existente:
                raise forms.ValidationError("Ya existe una cuota registrada para este mes y año.")

            return cleaned_data
 


class YearFilterForm(forms.Form):
    ano = forms.ChoiceField(choices=[(str(ano), str(ano)) for ano in range(2023, 2030)], label='Año')


class CuotaActividadForm(forms.ModelForm):
    class Meta:
        model = CuotaActividad
        fields = ('__all__')

    def clean(self):
        cleaned_data = super().clean()
        mes = cleaned_data.get('mes')
        año = cleaned_data.get('año')
        socio = cleaned_data.get('socio')

        # Realiza la validación personalizada para evitar cuotas duplicadas del mismo mes y año para el mismo socio
        if mes and año and socio:
            cuotas_duplicadas = CuotaActividad.objects.filter(
                mes=mes,
                año=año,
                socio=socio
            )
            if cuotas_duplicadas.exists():
                raise forms.ValidationError("Ya existe una cuota para este socio en el mismo mes y año.")

        return cleaned_data

class YearFilterForm2(forms.Form):
    ano = forms.ChoiceField(choices=[(str(ano), str(ano)) for ano in range(2023, 2030)], label='Año')