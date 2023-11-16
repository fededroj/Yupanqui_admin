from django.db import models

# Create your models here.
class Socio(models.Model):

    GENEROS = [
        (1,'Masculino'),
        (2,'Femenino'),
        (3,'Otro'),
            ]
    ESTADOS =[
        (1,'Activo'),
        (2,'Inactivo')
    ]
    nroSocio = models.IntegerField(verbose_name='Nro de Socio', unique=True ,null=False)
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    apellido = models.CharField(max_length=150,verbose_name='Apellido')
    genero = models.IntegerField(choices = GENEROS, default=1)
    email = models.EmailField(max_length=150,null=True)
    dni = models.IntegerField(verbose_name="DNI")
    tel = models.IntegerField(verbose_name='Tel')
    calle = models.CharField(max_length=100,verbose_name='Calle')
    nro = models.IntegerField(verbose_name='Nro')
    localidad= models.CharField(max_length=50, verbose_name='Localidad')
   
    foto = models.ImageField(upload_to='imagenes',null=True,verbose_name='Foto',blank=True)
    estado = models.IntegerField(choices=ESTADOS,default=1)
    observaciones_importantes=models.TextField(max_length=100, null=True, blank=True, verbose_name='Observaciones Importantes')
    def __str__(self):
        return f"{self.nroSocio}  -  {self.nombre}    {self.apellido}" 