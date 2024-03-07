from django.db import models

# Create your models here.
class Equipo(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    nobre_equipo = models.CharField(max_length=50, verbose_name="Nombre")
    img_bandera = models.TextField(unique=True,verbose_name="Bandera")
    img_escudo = models.TextField(unique=True,verbose_name="Escudo")

    def __str__(self):
        return self.nobre_equipo

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"
        db_table = "Equipo"


class Posicion(models.Model):
    id_posicion = models.AutoField(primary_key=True)
    nombre_posicion = models.CharField(max_length=50, verbose_name="Posicion jugador")
    descripcion_posicion = models.TextField(unique=True,verbose_name="descripcion de la posicion")

    def __str__(self):
        return self.nombre_posicion

    class Meta:
        verbose_name = "Posicion"
        verbose_name_plural = "Posiciones"
        db_table = "Posicion"



class Jugador(models.Model):
    id_jugador = models.AutoField(primary_key=True)
    nombre_jugador = models.CharField(max_length=50, verbose_name="Nombre jugador")
    apellido_jugador = models.TextField(max_length=50,verbose_name="Apellido jugador")
    foto = models.TextField(unique=True,verbose_name="Foto jugador")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento")
    posicion = models.ForeignKey(Posicion, on_delete=models.CASCADE, verbose_name="Posicion")
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, verbose_name="Equipo")
    numero_camiseta = models.TextField(max_length = 2,verbose_name="Numero de camiseta")
    titular = models.BooleanField(verbose_name="Titular")

    def __str__(self):
        return self.nombre_jugador

    class Meta:
        verbose_name = "Jugador"
        verbose_name_plural = "Jugadores"
        db_table = "Jugador"



class Roles(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=50, verbose_name="Nombre rol")

    def __str__(self):
        return self.nombre_rol

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"
        db_table = "Rol"



class Tecnico(models.Model):
    id_tecnico = models.AutoField(primary_key=True)
    nombre_tecnico = models.CharField(max_length=50, verbose_name="Nombre tecnico")
    apellido_tecnico = models.TextField(max_length=50,verbose_name="Apellido tecnico")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento")
    nacionalidad = models.TextField(max_length = 30,verbose_name="Nacionalidad")
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, verbose_name="Equipo")
    rol = models.ForeignKey(Roles, on_delete=models.CASCADE, verbose_name="Rol")


    def __str__(self):
        return self.nombre_jugador

    class Meta:
        verbose_name = "Tecnico"
        verbose_name_plural = "Tecnicos"
        db_table = "Tecnico"
