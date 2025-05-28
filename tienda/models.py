from django.db import models

class Electrodomestico(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100) 
    tipo = models.CharField(max_length=50, default='General')  # <-- Nuevo campo
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='electrodomesticos/')
    vendedor = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    electrodomestico = models.ForeignKey(Electrodomestico, related_name='comentarios', on_delete=models.CASCADE)
    nombre_usuario = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.nombre_usuario} sobre {self.electrodomestico.nombre}'