from django.db import models

# Create your models here.

class interesado(models.Model):
    Nombre = models.CharField(_("Nombre"), max_length=50)
    Apellido = models.CharField(_("Apellido"), max_length=50)
    Correo = models.EmailField(_("Correo"), max_length=254)
    Celular = models.CharField(_("Celular"), max_length=10)

    class Meta:
        db_table = 'interesado'
        
class bachillerato(models.Model):
    ID_Interesado = models.ForeignKey(interesado, verbose_name=_("Interesado"), on_delete=models.CASCADE, related_name='bachilleratos')
    Turno = models.CharField(_("Turno"), max_length=50)
    Carrera = models.CharField(_("Carrera"), max_length=50)
    Modalidad = models.CharField(_("Modalidad"), max_length=50)
    
    class Meta:
        db_table = 'bachillerato'
        
class licenciatura(models.Model):
    ID_Interesado = models.ForeignKey(interesado, verbose_name=_("Interesado"), on_delete=models.CASCADE, related_name='licenciaturas')
    Turno = models.CharField(_("Turno"), max_length=50)
    Carrera = models.CharField(_("Carrera"), max_length=50)
    Modalidad = models.CharField(_("Modalidad"), max_length=50)
    
    class Meta:
        db_table = 'licenciatura'
        
class grado_academico(models.Model):
    ID_Bachillerato = models.ForeignKey(bachillerato, verbose_name=_("Bachillerato"), on_delete=models.CASCADE, related_name='grados_academicos')
    ID_Licenciatura = models.ForeignKey(licenciatura, verbose_name=_("Licenciatura"), on_delete=models.CASCADE, related_name='grados_academicos')
    
    class Meta:
        db_table = 'grado_academico'
    
class visita(models.Model):
    ID_Interesado = models.ForeignKey(interesado, verbose_name=_("Interesado"), on_delete=models.CASCADE, related_name='visitas') 
    Fecha_Registro = models.DateTimeField(_("Fecha_Registro"), auto_now=False, auto_now_add=False)
    
    class Meta:
        db_table = 'visita'