from django.db import models

# Create your models here.

#CATEGORIA
class Categoria(models.Model):
    
    categoria=models.CharField(verbose_name="categoria", max_length=20, null=False)   
    
    
    def __str__(self):
       return f"{self.categoria}    "
    

#ACTIVIDAD

class Actividad(models.Model):
    nombre=models.CharField(verbose_name="Actividad", max_length=50, null=False) 
    categoria=models.ManyToManyField(Categoria)
    def __str__(self):
        return f" {self.nombre} "  
   

#PROFESOR

class Profesor(models.Model):
    id_profesor=models.IntegerField(null=False, verbose_name="id_profesor")
    categorias=models.ManyToManyField(Categoria)
    actividad= models.ForeignKey(Actividad,  on_delete=models.CASCADE, null= False)
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    apellido = models.CharField(max_length=150,verbose_name='Apellido')
    email = models.EmailField(max_length=150,null=True)
    dni = models.IntegerField(verbose_name="DNI")
    tel = models.IntegerField(verbose_name='Tel')
    calle = models.CharField(max_length=100,verbose_name='Calle')
    nro = models.IntegerField(verbose_name='Nro')
    localidad= models.CharField(max_length=50, verbose_name='Localidad')

    def __str__(self):
       return f"{self.nombre} -  {self.categorias}"
    