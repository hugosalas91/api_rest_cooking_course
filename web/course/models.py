from django.db import models


class Pupil(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, default='')
    cp = models.CharField(max_length=5)
    country_code = models.CharField(max_length=2)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('created',)
        
        
class CookingCourse(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    chef = models.ForeignKey('auth.User', related_name='cooking_courses', on_delete=models.CASCADE)
    pupils = models.ManyToManyField(Pupil)
    
    class Meta:
        ordering = ('created',)


class weather(models.Model):
    lon_coord = models.FloatField(default="0.0", verbose_name="Longitud")
    lat_coord = models.FloatField(default="0.0", verbose_name="Latitud")
    type_sys = models.IntegerField(default="0", verbose_name="Tipo")
    id_sys = models.IntegerField(default="0", verbose_name="Id sys")
    message_sys = models.FloatField(default="0.0", verbose_name="Mensaje")
    country_sys = models.CharField(max_length=2, verbose_name="País")
    sunrise_sys = models.IntegerField(default="0", verbose_name="Salida del sol")
    sunset_sys = models.IntegerField(default="0", verbose_name="Puesta del sol")
    id_weather = models.IntegerField(default="0", verbose_name="Id weather")
    main_weather = models.CharField(max_length=80, verbose_name="Tiempo meteorológico principal")
    description_weather = models.CharField(max_length=200, verbose_name="Descripción")
    icon_weather = models.CharField(max_length=80, verbose_name="Icono")
    base = models.CharField(max_length=80, verbose_name="Base")
    temp_main = models.FloatField(default="0.0", verbose_name="Temperatura")
    humidity_main = models.FloatField(default="0.0", verbose_name="Humedad")
    pressure_main = models.FloatField(default="0.0", verbose_name="Presión")
    temp_min_main = models.FloatField(default="0.0", verbose_name="Temperatura mínima")
    temp_max_main = models.FloatField(default="0.0", verbose_name="Temperatura máxima")
    speed_wind = models.FloatField(default="0.0", verbose_name="Velocidad del viento")
    deg_wind = models.FloatField(default="0.0", verbose_name="Deg del viento")
    clouds = models.FloatField(default="0.0", verbose_name="Nubes")
    dt = models.IntegerField(default="0", verbose_name="Dt")
    id = models.IntegerField(default="0", verbose_name="Id")
    name = models.CharField(max_length=80, verbose_name="Nombre")
    cod = models.IntegerField(default="0", verbose_name="Cod")
    