from django.db import models

# Create your models here.
class Banda(models.Model):
    nombre=models.CharField(max_length=30)
    genero=models.CharField(max_length=30,choices=[("Pop","pop"),("Rock","rock"),("Jazz","jazz")])
    origen=models.CharField(max_length=30)
    fecha_creada=models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.nombre}-{self.genero}-{self.origen}-{self.fecha_creada}"
    
class Solista(models.Model): 
    nombre=models.CharField(max_length=30)
    genero=models.CharField(max_length=30,choices=[("Pop","pop"),("Reggaeton","reggaeton"),("Rap","rap")])
    origen=models.CharField(max_length=30)
    edad=models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.nombre}-{self.genero}-{self.origen}-{self.edad}"
    