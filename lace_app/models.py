from os import truncate
from django.db import models
from datetime import datetime
from django.urls import reverse
from django.utils.timezone import now
#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
#-------------------------------------- LACE ----------------------------------------------------------------------
class SucursalLACE(models.Model):
    idsucursal = models.CharField(
        verbose_name= 'ID Sucursal',
        max_length= 45
        )
    calle = models.CharField(
        verbose_name= 'Calle',
        max_length= 45,
        blank= True,
        null= True
        )
    colonia = models.CharField(
        verbose_name= 'Colonia',
        max_length= 45,
        blank= True,
        null= True
        )
    delegacion_municipio = models.CharField(
        verbose_name= 'Alcaldía/Municipio',
        max_length= 100,
        blank= True,
        null= True
        )
    entidadfed = models.CharField(
        verbose_name= 'Entidad Federativa',
        max_length= 100,
        blank= True,
        null= True
        )
    pais = models.CharField(
        verbose_name= 'País',
        max_length= 45,
        blank= True,
        null= True
        )
    noint = models.CharField(
        verbose_name= 'No. Interior',
        max_length= 45,
        blank= True,
        null= True
        )
    noext = models.CharField(
        verbose_name= 'No. Exterior',
        max_length= 45,
        blank= True,
        null= True
        )

    class Meta:
        verbose_name = 'Sucursal LACE'
        verbose_name_plural = 'Sucursales LACE'

    def __str__(self):
        return str(self.idsucursal)


class Departamento(models.Model):
    iddepto = models.CharField(
        verbose_name='ID Departamento',
        primary_key=True,
        max_length=45
    )
    nombredepto = models.CharField(
        verbose_name='Nombre de Departamento',
        max_length=45,
        blank=True,
        null=True
    )
    id_sucursal = models.ForeignKey(
        SucursalLACE,
        on_delete=models.CASCADE,
        verbose_name="Sucursal LACE",
    )

    class Meta:
        verbose_name = 'Departamento LACE'
        verbose_name_plural = 'Departamentos LACE'

    def __str__(self):
        return str(self.nombredepto)


class Empleado(models.Model):
    idempleado = models.CharField(
        verbose_name= 'ID Empleado',
        max_length= 45
    )
    nombre_s_field = models.CharField(
        verbose_name= 'Nombre(s)',
        max_length= 100,
        blank= True,
        null= True
    )
    apellidopaterno = models.CharField(
        verbose_name= 'Apellido Paterno',
        max_length= 45,
        blank= True,
        null= True
    )
    apellidomaterno = models.CharField(
        verbose_name= 'Apellido Materno',
        max_length= 45,
        blank= True,
        null= True
    )
    calle = models.CharField(
        verbose_name= 'Calle',
        max_length= 45,
        blank= True,
        null= True
    )
    alcaldia_municipio = models.CharField(
        verbose_name= 'Alcaldía/Municipio',
        max_length= 100,
        blank= True,
        null= True
    )
    colonia = models.CharField(
        verbose_name= 'Colonia',
        max_length= 45,
        blank= True,
        null= True
    )
    entidadfed = models.CharField(
        verbose_name= 'Entidad Federativa',
        max_length= 100,
        blank= True,
        null= True
    )
    pais = models.CharField(
        verbose_name= 'País',
        max_length= 45,
        blank= True,
        null= True
    )  
    codigopostal = models.CharField(
        verbose_name= 'Código Postal',
        max_length= 45,
        blank= True,
        null= True
    )
    manzana = models.CharField(
        verbose_name= 'Manzana',
        max_length= 45,
        blank= True,
        null= True
    )
    lote = models.CharField(
        verbose_name= 'Lote',
        max_length= 45,
        blank= True,
        null= True
    )
    email = models.CharField(
        verbose_name= 'Correo Electrónico',
        max_length= 45,
        blank= True,
        null= True
    )
    nacionalidad = models.CharField(
        verbose_name= 'Nacionalidad',
        max_length= 45,
        blank= True,
        null= True
    )
    fechanacimiento = models.DateTimeField(
        verbose_name= 'Fecha de Nacimiento',
        blank= True,
        null= True
    )
    escolaridad = models.CharField(
        verbose_name= 'Escolaridad',
        max_length= 45,
        blank= True,
        null= True
    )
    dependienteseco = models.IntegerField(
        verbose_name= 'No. de Dependientes Económicos',
        blank= True,
        null= True
    )
    estadocivil = models.CharField(
        verbose_name= 'Estado Civil',
        max_length= 50,
        blank= True,
        null= True
    )
    nolicencia = models.CharField(
        verbose_name= 'No. de Licencia de Conducir',
        max_length= 100,
        blank= True,
        null= True
    )
    rfc = models.CharField(
        verbose_name= 'RFC',
        max_length=50,
        blank= True,
        null= True
    )
    noimss = models.CharField(
        verbose_name= 'No. Seguridad Social',
        max_length= 50,
        blank= True,
        null= True
    )
    nombreconyuge = models.CharField(
        verbose_name= 'Nombre de Conyuge',
        max_length= 100,
        blank= True,
        null= True
    )
    umf = models.CharField(
        verbose_name= 'Unidad Médico Familiar',
        max_length= 50,
        blank= True,
        null= True
    )
    id_sucursal = models.ForeignKey(
        SucursalLACE,
        on_delete=models.CASCADE,
        verbose_name="Sucursal LACE",
    )
    id_depto = models.ForeignKey(
        Departamento,
        on_delete=models.CASCADE,
        verbose_name="Departamento LACE",
    )

    class Meta:
        db_table = 'empleado'
        verbose_name = 'Empleado LACE'
        verbose_name_plural = 'Empleados LACE'

    def __str__(self):
        return str(self.idempleado)
#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
#-------------------------------------- Clientes -----------------------------------------------------
class ClienteEmpresa(models.Model):
    id_empresa = models.CharField(
        verbose_name='ID Cliente',
        max_length=45
    )
    razonsocial = models.CharField(
        verbose_name='Razón Social',
        max_length=100,
        blank=True,
        null=True
    )
    nombrepila = models.CharField(
        verbose_name='Nombre de Pila',
        max_length=45,
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'clienteempresa'
        verbose_name = 'Cliente Empresa'
        verbose_name_plural = 'Clientes Empresas'

    def __str__(self):
        return str(self.id_empresa) + " - " + str(self.nombrepila)
#---------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------- Documentación Clientes -------------------------------------------------------------
#------------------------------------------------- Facturación -------------------------------------------------------------------
#----------------------------------------------------- UsoCFDI -------------------------------------------------------------------
class Usocfdi(models.Model):
    opcion = models.CharField(
        verbose_name='CFDI',
        max_length=50,
    )

    class Meta:
        db_table = 'usocfdi'
        verbose_name = 'CFDI'
        verbose_name_plural = 'CFDIs'

    def __str__(self):
        return str(self.opcion)

#----------------------------------------------------- Forma de Pago -------------------------------------------------------------------
class Formapago(models.Model):
    opcion = models.CharField(
        verbose_name='Forma de pago',
        max_length=50,
    )

    class Meta:
        db_table = 'formapago'
        verbose_name = 'Forma de Pago'
        verbose_name_plural = 'Formas de Pago'

    def __str__(self):
        return str(self.opcion)

#----------------------------------------------------- Método de Pago -------------------------------------------------------------------
class Metodopago(models.Model):
    opcion = models.CharField(
        verbose_name='Método de Pago',
        max_length=50,
    )

    class Meta:
        db_table = 'metodopago'
        verbose_name = 'Método de Pago'
        verbose_name_plural = 'Métodos de Pago'

    def __str__(self):
        return str(self.opcion)

#----------------------------------------------------- Facturación -------------------------------------------------------------------
class Facturacion(models.Model):
    rfc = models.CharField(
        verbose_name='RFC',
        max_length=45
    )
    email = models.CharField(
        verbose_name='Correo Electrónico',
        max_length=45,
        blank=True,
        null=True
    )
    calle = models.CharField(
        verbose_name='Calle',
        max_length=45,
        blank=True,
        null=True
    )
    noint = models.CharField(
        verbose_name='No. Interior',
        max_length=45,
        blank=True,
        null=True
    )
    noext = models.CharField(
        verbose_name='No. Exterior',
        max_length=45,
        blank=True,
        null=True
    )
    codigopostal = models.CharField(
        verbose_name='Código Postal',
        max_length=45,
        blank=True,
        null=True
    )
    alcaldia_municipio = models.CharField(
        verbose_name='Alcaldía/Municipio',
        max_length=100,
        blank=True,
        null=True
    )  
    colonia = models.CharField(
        verbose_name='Colonia',
        max_length=45,
        blank=True,
        null=True
    )
    entidadfed = models.CharField(
        verbose_name='Entidad Federativa',
        max_length=100,
        blank=True,
        null=True
    )
    pais = models.CharField(
        verbose_name='País',
        max_length=45,
        blank=True,
        null=True
    )
    usocfdi = models.ForeignKey(
        Usocfdi,
        on_delete=models.CASCADE,
        verbose_name='CFDI',
    )
    metodopago = models.ForeignKey(
        Metodopago,
        on_delete=models.CASCADE,
        verbose_name='Método de Pago',
    )
    formapago = models.ForeignKey(
        Formapago,
        on_delete=models.CASCADE,
        verbose_name='Forma de Pago',
    )
    id_empresa = models.ForeignKey(
        ClienteEmpresa,
        on_delete=models.CASCADE,
        verbose_name="Cliente - Empresa",
    )

    class Meta: 
        db_table = 'facturacion'
        verbose_name = 'Facturación'
        verbose_name_plural = 'Facturación'

    def __str__(self):
        return str(self.rfc)

#----------------------------------------------------- Certificado -------------------------------------------------------------------
class Certificado(models.Model):
    razonsocial = models.CharField(
        verbose_name='Razón Social',
        max_length=45,
        blank=True,
        null=True
    )
    atencion = models.CharField(
        verbose_name='Atención con',
        max_length=45,
        blank=True,
        null=True
    )
    calle = models.CharField(
        verbose_name='Calle',
        max_length=45,
        blank=True,
        null=True
    )
    noint = models.CharField(
        verbose_name='No. Interior',
        max_length=45,
        blank=True,
        null=True
    )
    noext = models.CharField(
        verbose_name='No. Exterior',
        max_length=45,
        blank=True,
        null=True
    )
    codigopostal = models.CharField(
        verbose_name='Código Postal',
        max_length=45,
        blank=True,
        null=True
    )
    colonia = models.CharField(
        verbose_name='Colonia',
        max_length=45,
        blank=True,
        null=True
    )
    alcaldia_municipio = models.CharField(
        verbose_name='Alcaldía/Municipio',
        max_length=100,
        blank=True,
        null=True
    )
    entidadfed = models.CharField(
        verbose_name='Entidad Federativa',
        max_length=100,
        blank=True,
        null=True
    )
    pais = models.CharField(
        verbose_name='País',
        max_length=45,
        blank=True,
        null=True
    )
    id_empresa = models.ForeignKey(
        ClienteEmpresa,
        on_delete=models.CASCADE,
        verbose_name="Cliente",
    )

    class Meta:
        db_table = 'certificado'
        verbose_name = 'Certificado'
        verbose_name_plural = 'Certificados'

    def __str__(self):
        return str(self.razonsocial + ' - ' + self.atencion)

#----------------------------------------------------- Contacto -------------------------------------------------------------------
class Contacto(models.Model): 
    puesto = models.CharField(
        verbose_name='Puesto',
        max_length=45,
        blank=True,
        null=True
    )
    departamento = models.CharField(
        verbose_name='Departamento',
        max_length=45,
        blank=True,
        null=True
    )
    nombre = models.CharField(
        verbose_name='Nombre(s)',
        max_length=100,
        blank=True,
        null=True
    ) 
    apellidopaterno = models.CharField(
        verbose_name='Apellido Paterno',
        max_length=45,
        blank=True,
        null=True
    ) 
    apellidomaterno = models.CharField(
        verbose_name='Apellido Materno',
        max_length=45,
        blank=True,
        null=True
    )
    correo = models.CharField(
        verbose_name='Correo Electrónico',
        max_length=45,
        blank=True,
        null=True
    )
    telefono = models.CharField(
        verbose_name='Teléfono',
        max_length=45,
        blank=True,
        null=True
    ) 
    extension = models.CharField(
        verbose_name='Extensión',
        max_length=45,
        blank=True,
        null=True
    )
    celular = models.CharField(
        verbose_name='Celular',
        max_length=45,
        blank=True,
        null=True
    )
    enviar_certificado = models.BooleanField(
        verbose_name= "Enviar Certificado",
        default= False,
        null= False,
        blank= False
    )
    enviar_factura = models.BooleanField(
        verbose_name= "Enviar Facturación",
        default= False,
        null= False,
        blank= False
    )
    enviar_orden = models.BooleanField(
        verbose_name= "Enviar Orden de Servicio",
        default= False,
        null= False,
        blank= False
    )
    id_empresa = models.ForeignKey(
        ClienteEmpresa,
        on_delete=models.CASCADE,
        verbose_name="Cliente - Empresa",
    )
    conctacto_predeterminado = models.BooleanField(
        verbose_name= "Contacto Predeterminado",
        default= False,
        null= False,
        blank= False
    )

    class Meta:
        db_table = 'contacto'
        verbose_name = 'Perfil de Contacto'
        verbose_name_plural = 'Perfiles de Contacto'

    def __str__(self):
        return str(self.puesto)

#----------------------------------------------------- Sitio -------------------------------------------------------------------
class Sitio(models.Model):
    telefono = models.CharField(
        verbose_name='Teléfono',
        max_length=45,
        blank=True,
        null=True
    )
    email = models.CharField(
        verbose_name='Correo Electrónico',
        max_length=45,
        blank=True,
        null=True
    )
    calle = models.CharField(
        verbose_name='Calle',
        max_length=45,
        blank=True,
        null=True
    )
    noint = models.CharField(
        verbose_name='No. Interior',
        max_length=45,
        blank=True,
        null=True
    )
    noext = models.CharField(
        max_length=45,
        blank=True,
        null=True
    )
    codigopostal = models.CharField(
        verbose_name='Código Postal',
        max_length=45,
        blank=True,
        null=True
    )
    colonia = models.CharField(
        verbose_name='Colonia',
        max_length=45,
        blank=True,
        null=True
    )
    alcaldia_municipio = models.CharField(
        verbose_name='Alcaldía/Municipio',
        max_length=45,
        blank=True,
        null=True
    )
    entidadfed = models.CharField(
        verbose_name='Entidad Federativa',
        max_length=45,
        blank=True,
        null=True
    )
    pais = models.CharField(
        verbose_name='País',
        max_length=45,
        blank=True,
        null=True
    )
    id_empresa = models.ForeignKey(
        ClienteEmpresa,
        on_delete=models.CASCADE,
        verbose_name="Cliente - Empresa",
    )

    class Meta:
        db_table = 'sitio'
        verbose_name = 'Perfil de Recolección'
        verbose_name_plural = 'Perfiles de Recolección'

    def __str__(self):
        return str("Sitio de {} - {}".format(self.id_empresa,self.id))

#------------------------------------------------- Recolección y Entrega --------------------------------------------------------
class RecoleccionEntrega(models.Model):
    atencion = models.CharField(
        verbose_name= "Atención con",
        max_length= 50,
        blank= True,
        null= True,
    )
    observaciones_re = models.CharField(
        verbose_name= "Observaciones",
        max_length= 255,
        blank= True,
        null= True,
    )
    recoleccion = models.BooleanField(
        verbose_name= "Es Recolección",
        default= False,
    )
    entrega = models.BooleanField(
        verbose_name= "Es Entrega",
        default= False,
    )
    id_sitio = models.ForeignKey(
        Sitio,
        verbose_name= "Sitio",
        on_delete= models.CASCADE,
        blank= True,
        null= True
    )
    id_empresa = models.ForeignKey(
        ClienteEmpresa,
        verbose_name= "Cliente/Empresa",
        on_delete= models.CASCADE,
        blank= True,
        null= True
    )

    class Meta:
        db_table = "RecoleccionEntrega"
        verbose_name = "Recolección y Entrega"
        verbose_name_plural = "Recolecciones y Entregas"
        
    def __str__(self):
        return "RE-" + str(self.id).zfill(3)

#------------------------------------------------- Servicio en Sitio --------------------------------------------------------
class EPP(models.Model):
    opcion = models.CharField(
        verbose_name= "Opción",
        max_length= 100,
        blank= True,
        null= True,
    )

    class Meta:
        db_table = "EPP"
        verbose_name = "Equipo de Protección Personal (EPP)"
        verbose_name_plural = "Equipo de Protección Personal (EPP)"

    def __str__(self):
        return self.opcion


class ServicioSitio(models.Model):
    id_sitio = models.ForeignKey(
        Sitio,
        verbose_name= "Sitio",
        on_delete= models.CASCADE,
        blank= True,
        null= True
    )
    id_empresa = models.ForeignKey(
        ClienteEmpresa,
        verbose_name= "Cliente/Empresa",
        on_delete= models.CASCADE,
        blank= True,
        null= True
    )
    epp = models.ManyToManyField(
        EPP,
        related_name= "equipoproteccion",
        verbose_name= "Equipo de Protección Personal (EPP)"
    )
    epp_option = models.CharField(
        verbose_name = "Otro Equipo de Protección Personal (EPP)",
        max_length= 100,
        blank= True,
        null= True
    )

    class Meta:
        verbose_name = "Servicio en Sitio"
        verbose_name_plural = "Servicios en Sitio"

    def __str__(self):
        return "SS-" + str(self.id).zfill(3)

#------------------------------------------------- Subcontratación -------------------------------------------------------------------
class TerceriaSubcontratacion(models.Model):
    razonsocial = models.CharField(
        verbose_name= "Razón Social",
        max_length= 50,
        blank= True,
        null= True
    )
    id_sitio = models.ForeignKey(
        Sitio,
        verbose_name= "Sitio",
        on_delete= models.CASCADE,
        blank= True,
        null= True
    )
    id_empresa = models.ForeignKey(
        ClienteEmpresa,
        verbose_name= "Cliente/Empresa",
        on_delete= models.CASCADE,
        blank= True,
        null= True
    )

    class Meta:
        verbose_name = "Sitio de Subcontratación"
        verbose_name_plural = "Sitios de Subcontratación"

    def __str__(self):
        return "TS-" + str(self.id).zfill(3)

#------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------- Instrumentos -------------------------------------------------------------------
#----------------------------------------------------- Área/Magnitud ----------------------------------------------------------------
class AreaMagnitud(models.Model):
    opcion = models.CharField(
        verbose_name='Opción',
        max_length=100,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Área/Magnitud'
        verbose_name_plural = 'Área/Magnitud'

    def __str__(self):
        return str(self.opcion)

#----------------------------------------------------- Bigencia ----------------------------------------------------------------
class Vigencia(models.Model):
    opcion = models.CharField(
        verbose_name='Opción',
        max_length=100,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Vigencia'
        verbose_name_plural = 'Vigencias'

    def __str__(self):
        return str(self.opcion)


class FechaCalibracion(models.Model):
    ultima_calibracion = models.DateField(
        verbose_name= "Última Fecha de Calibración",
        auto_now_add= True,
    )
    id_instrumento = models.ForeignKey(
        "Instrumento",
        verbose_name= "Instrumentos",
        on_delete= models.CASCADE,
        blank= True,
        null= True
    )
    id_vigencia = models.ForeignKey(
        Vigencia,
        verbose_name= "Vigencia",
        on_delete= models.CASCADE,
        blank= True,
        null= True
    )


#----------------------------------------------------- Tipo de SErvicio ---------------------------------------------------------
class ServicioInstrumento(models.Model):
    opcion = models.CharField(
        verbose_name='Opción',
        max_length=100,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Servicio a Instrumento'
        verbose_name_plural = 'Servicios a Instrumento'

    def __str__(self):
        return str(self.opcion)

#----------------------------------------------------- Fotografías de Instrumentos --------------------------------------------------
class Fotografia(models.Model):
    imagen = models.ImageField(
        verbose_name= "Fotografía",
        upload_to= "img"
    )

    class Meta:
        verbose_name = 'Instrumento Fotografía'
        verbose_name_plural = 'Instrumento Fotografías'

    def __str__(self):
        return str(self.id)


class InstrumentosImagen(models.Model):
    observaciones_ii = models.CharField(
        verbose_name= "Observaciones",
        max_length= 255,
        blank= True,
        null= True,
    )
    id_fotografia = models.ForeignKey(
        Fotografia,
        verbose_name= "Fotografías",
        on_delete= models.CASCADE,
        blank= True,
        null= True
    )
    id_instrumento = models.ForeignKey(
        "Instrumento",
        verbose_name= "Instrumentos",
        on_delete= models.CASCADE,
        blank= True,
        null= True
    )
    
#---------------------------------------------------------- Instrumentos ---------------------------------------------------------------
class Instrumento(models.Model):
    clave_id = models.CharField(
        verbose_name='Clave/ID',
        max_length=45,
        blank= True,
        null= False
    )
    nombre_instrumento = models.CharField(
        verbose_name= 'Nombre de instrumento',
        max_length= 45,
        blank= True,
        null= True
    )
    marca = models.CharField(
        verbose_name= 'Marca',
        max_length= 45,
        blank= True,
        null= True
    )
    modelo = models.CharField(
        verbose_name= 'Modelo',
        max_length= 45,
        blank= True,
        null= True
    )
    serie = models.CharField(
        verbose_name= 'Serie',
        max_length= 45,
        blank= True,
        null= True
    )
    intervalooperacion = models.CharField(
        verbose_name= 'Intervalo de Operación',
        max_length= 45,
        blank= True,
        null= True
    )
    alcance = models.CharField(
        verbose_name= 'Alcance',
        max_length= 45,
        blank= True,
        null= True
    )
    exactitud = models.CharField(
        verbose_name= 'Exactitud',
        max_length= 45,
        blank= True,
        null= True
    )
    emt = models.CharField(
        verbose_name= 'Error Máximo Tolerado',
        max_length= 45,
        blank= True,
        null= True
    )
    divisionminima = models.CharField(
        verbose_name= 'División Mínima',
        max_length= 45,
        blank= True,
        null= True
    )
    puntoscalibracion = models.CharField(
        verbose_name= 'Puntos de Calibración',
        max_length= 255,
        blank= True,
        null= True
    )
    id_empresa = models.ForeignKey(
        ClienteEmpresa,
        on_delete=models.CASCADE,
        verbose_name="Cliente/Empresa",
    )
    id_sitio = models.ForeignKey(
        Sitio,
        on_delete= models.CASCADE,
        verbose_name= "Sitio"
    )
    areamagnitud = models.ManyToManyField(
        AreaMagnitud,
        verbose_name= "Área/Magnitud",
    )
    
    class Meta:
        verbose_name = 'Instrumento'
        verbose_name_plural = 'Instrumentos'

    def __str__(self):
        magnitudes = ""
        if (len(self.areamagnitud.all()) > 1):
            magnitudes += self.areamagnitud.all().__str__()
        else:
            for magnitud in self.areamagnitud.all():
                magnitudes += magnitud.__str__() + ", "

            magnitudes = magnitudes[0:-2]
        cadena = "{} - {} - ({})".format(self.clave_id, self.nombre_instrumento, magnitudes)
        return cadena



class InstrumentOS(models.Model):
    id_instrumento = models.ForeignKey(
        Instrumento,
        verbose_name= "Clave/ID Instrumento",
        on_delete= models.CASCADE,
        blank= True,
        null= True
    )
    id_servicio = models.ManyToManyField(
        ServicioInstrumento,
        verbose_name= "Servicio Solicitado"
    )
    id_imagen = models.ManyToManyField(
        Fotografia,
        verbose_name= "Fotografías de Instrumento"
    )
    id_vigencia = models.ForeignKey(
        Vigencia,
        verbose_name= "Vigencia",
        on_delete= models.CASCADE,
        blank= True,
        null= True
    )
    id_OSSubServicio = models.ForeignKey(
        "SubServicio",
        verbose_name= "Pertenece a la OS-SS",
        on_delete= models.CASCADE,
        blank= True,
        null= True
    )
    ultima_calibracion = models.DateField(
        verbose_name= "Última Fecha de Calibración",
        auto_now_add= True,
    )
    observaciones_ios = models.CharField(
        verbose_name= "Observaciones",
        max_length= 255,
        blank= True,
        default= "Sin Observaciones"
    )
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------- Modelos para la Orden de Servicio ------------------------------------------------
#------------------------------------------------------------- Estatus --------------------------------------------------------------
class Estatus(models.Model):
    options = models.CharField(
        verbose_name = 'Opciones',
        max_length = 50,
    )

    class Meta:
        db_table = 'estatus'
        verbose_name = "Estatus de Proceso"
        verbose_name_plural = "Estatus de Proceso"

    def __str__(self):
        return str(self.options)

#--------------------------------------------------------- Tipo de Servicio --------------------------------------------------------------
class tipoServicio(models.Model):
    opcion = models.CharField(
        verbose_name= "Opción",
        max_length= 25,
        blank= True,
        null= True,
    )

    class Meta:
        db_table = "tipoServicio"
        verbose_name = "Tipo de Servicio"
        verbose_name_plural = "Tipos de Servicios"

    def __str__(self):
        return self.opcion
#-------------------------------------------------------- Orden de Servicio --------------------------------------------------------------
class OrdenServicio(models.Model):
    dia_servicio = models.DateTimeField(
        verbose_name = "Día y hora de Ingreso a Laboratorio",
    )
    dia_registro = models.DateTimeField(
        verbose_name = "Día de Registro de Orden",
        auto_now_add= True
    )
    id_orden = models.CharField(
        verbose_name = "Solicitud de Servicio",
        max_length = 45,
        blank= True,
        null= True
    )
    no_certificado = models.CharField(
        verbose_name = "Número de Certificado",
        max_length = 45,
        blank= True,
        null= True,
    )
    observaciones_os = models.CharField(
        verbose_name = "Observaciones",
        max_length = 255,
        blank=True,
        default= "Sin Observaciones"
    )
    id_cliente = models.ForeignKey(
        ClienteEmpresa,
        verbose_name= "Cliente/Empresa",
        on_delete= models.CASCADE,
        blank= True,
        null= True,
    )
    id_contacto = models.ForeignKey(
        Contacto,
        verbose_name= "Contacto",
        on_delete= models.CASCADE,
        blank= True,
        null= True,
    )
    estatus = models.ForeignKey(
        Estatus,
        on_delete= models.CASCADE,
        verbose_name= "Estatus de proceso",
        blank= True,
        null= True
    )
    id_subservicio = models.ManyToManyField(
        "SubServicio",
        related_name= "sub_servicio_os",
        verbose_name= "SubServicio"
    )

    class Meta:
        db_table = "services"
        verbose_name = "Orden de Servicio"
        verbose_name_plural = "Ordenes de Servicios"

    def __str__(self):
        return str(self.id_orden)

    def get_absolute_url(self):
        return reverse("ordenes_servicio:service_order_detail", kwargs={"id": self.id})

#--------------------------------------------------- Sub-Servicios ----------------------------------------------------------
class SubServicio(models.Model):
    id_facturacion = models.ForeignKey(
        Facturacion,
        verbose_name= "Facturación",
        on_delete= models.CASCADE,
        blank= True,
        null= True,
    )
    id_certificado = models.ForeignKey(
        Certificado,
        verbose_name = "Datos de Certificado",
        on_delete= models.CASCADE,
        blank= True,
        null= True,
    )
    id_sitio = models.ForeignKey(
        Sitio,
        on_delete = models.CASCADE,
        verbose_name = "Sitio"
    )
    id_instrumento = models.ManyToManyField(
        'Instrumento',
        related_name = "Instrumento",
        verbose_name = 'Instrumento'
    )
    servicioContratado = models.ForeignKey(
        tipoServicio,
        on_delete= models.CASCADE,
        verbose_name= "Tipo de servicio requerido",
        blank= False,
        null= True,
    )

    class Meta:
        verbose_name = "Sub-Servicio"
        verbose_name_plural = "Sub-Servicios"
    
    def __str__(self):
        return str(self.id)

# class Contratacion(models.Model):
#     fechaingreso = models.CharField(db_column='FechaIngreso', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     puesto = models.CharField(db_column='Puesto', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     tipocontrato = models.CharField(db_column='TipoContrato', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     periodopago = models.CharField(db_column='PeriodoPago', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     tipojornada = models.CharField(db_column='TipoJornada', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     fechaantiguedad = models.CharField(db_column='FechaAntiguedad', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     tiposangre = models.CharField(db_column='TipoSangre', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     empleado_idempleado = models.OneToOneField('Empleado', models.DO_NOTHING, db_column='Empleado_IDEmpleado', primary_key=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'contratacion'


# class Director(models.Model):
#     iddirector = models.CharField(db_column='IDDirector', max_length=45)  # Field name made lowercase.
#     fechainicio = models.DateField(db_column='FechaInicio')  # Field name made lowercase.
#     sucursal_idsucursal = models.OneToOneField('Sucursal', models.DO_NOTHING, db_column='Sucursal_IDSucursal', primary_key=True)  # Field name made lowercase.
#     empleado_idempleado = models.ForeignKey('Empleado', models.DO_NOTHING, db_column='Empleado_IDEmpleado')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'director'
#         unique_together = (('sucursal_idsucursal', 'empleado_idempleado'),)


# class Familiar(models.Model):
#     rfc = models.CharField(db_column='RFC', max_length=45)  # Field name made lowercase.
#     nombre_s_field = models.CharField(db_column='Nombre(s)', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     apellidopaterno = models.CharField(db_column='ApellidoPaterno', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     apellidomaterno = models.CharField(db_column='ApellidoMaterno', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     parentesco = models.CharField(db_column='Parentesco', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     empleado_idempleado = models.OneToOneField(Empleado, models.DO_NOTHING, db_column='Empleado_IDEmpleado', primary_key=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'familiar'


# class Horario(models.Model):
#     horarioentrada = models.TimeField(db_column='HorarioEntrada')  # Field name made lowercase.
#     horariosalida = models.TimeField(db_column='HorarioSalida')  # Field name made lowercase.
#     diasdescanso = models.CharField(db_column='DiasDescanso', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     horariosabado = models.CharField(db_column='HorarioSabado', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     horariocomida = models.CharField(db_column='HorarioComida', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     horariocol = models.CharField(db_column='Horariocol', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     empleado_idempleado = models.OneToOneField(Empleado, models.DO_NOTHING, db_column='Empleado_IDEmpleado', primary_key=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'horario'



# class Mobiliario(models.Model):
#     serie = models.CharField(db_column='Serie', primary_key=True, max_length=255)  # Field name made lowercase.
#     modelo = models.CharField(db_column='Modelo', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     marca = models.CharField(db_column='Marca', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='Descripcion', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ubicacion = models.CharField(db_column='Ubicacion', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     sucursal_idsucursal = models.ForeignKey('Sucursal', models.DO_NOTHING, db_column='Sucursal_IDSucursal')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'mobiliario'


# class Proveedor(models.Model):
#     idproveedor = models.CharField(db_column='IDProveedor', primary_key=True, max_length=15)  # Field name made lowercase.
#     nombreproveedor = models.CharField(db_column='NombreProveedor', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     rfc = models.CharField(db_column='RFC', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     giro = models.CharField(db_column='Giro', max_length=45, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'proveedor'


# class Proveedorsucursal(models.Model):
#     proveedor_idproveedor = models.OneToOneField(Proveedor, models.DO_NOTHING, db_column='Proveedor_IDProveedor', primary_key=True)  # Field name made lowercase.
#     sucursal_idsucursal = models.ForeignKey('Sucursal', models.DO_NOTHING, db_column='Sucursal_IDSucursal')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'proveedorsucursal'
#         unique_together = (('proveedor_idproveedor', 'sucursal_idsucursal'),)



# class Supervisor(models.Model):
#     fechainicio = models.DateField(db_column='FechaInicio')  # Field name made lowercase.
#     departamento_iddepto = models.OneToOneField(Departamento, models.DO_NOTHING, db_column='Departamento_IDDepto', primary_key=True)  # Field name made lowercase.
#     empleado_idempleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='Empleado_IDEmpleado')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'supervisor'
#         unique_together = (('departamento_iddepto', 'empleado_idempleado'),)



# class Vehiculo(models.Model):
#     idvehiculo = models.CharField(db_column='IDVehiculo', primary_key=True, max_length=45)  # Field name made lowercase.
#     modelo = models.CharField(db_column='Modelo', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     marca = models.CharField(db_column='Marca', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     year = models.CharField(db_column='Año', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     noplaca = models.CharField(db_column='NoPlaca', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     sucursal_idsucursal = models.ForeignKey(Sucursal, models.DO_NOTHING, db_column='Sucursal_IDSucursal')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'vehiculo'



#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------#---------------------------------------- FACTURACIÓN ------------------------------------------------------
#------------------------------------- CRUD Recursos humanos ------------------------------------------------------
