from django import template

register = template.Library()

@register.filter
def months_iterator(ano):
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    return [(mes, meses[mes - 1]) for mes in range(1, 13)]

@register.filter
def get_month_value(mes, cuotas):
    cuota = cuotas.filter(mes=mes).first()
    return cuota
