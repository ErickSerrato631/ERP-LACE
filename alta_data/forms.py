from django.shortcuts import render
from django import forms
from lace_app import models as lace_models


class ClientsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if not 'Checkbox' in str(visible.field.widget):
                visible.field.widget.attrs['style'] = 'text-transform:uppercase'

    class Meta:
        model = lace_models.ClienteEmpresa
        fields = (
            'id_empresa',
            'razonsocial',
            'nombrepila',
            )


class CertificateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if not 'Checkbox' in str(visible.field.widget):
                visible.field.widget.attrs['style'] = 'text-transform:uppercase'

    class Meta:
        model = lace_models.Certificado
        fields = '__all__'
        widgets = {
            'id_empresa': forms.Select(attrs={'class': 'select-item'}),
        }

class BillingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if not 'Checkbox' in str(visible.field.widget):
                visible.field.widget.attrs['style'] = 'text-transform:uppercase'

    class Meta:
        model = lace_models.Facturacion
        fields = (
            'id_empresa',
            'rfc',
            'usocfdi',
            'metodopago',
            'formapago',
            'email',
            'calle',
            'noint',
            'noext',
            'codigopostal',
            'colonia',
            'alcaldia_municipio',
            'entidadfed',
            'pais',
        )
        widgets = {
            'id_empresa': forms.Select(attrs={'class': 'select-item'}),
            'usocfdi': forms.Select(attrs={'class': 'select-item'}),
            'metodopago': forms.Select(attrs={'class': 'select-item'}),
            'formapago': forms.Select(attrs={'class': 'select-item'}),
        }

class ContactProfieForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if not 'Checkbox' in str(visible.field.widget):
                visible.field.widget.attrs['style'] = 'text-transform:uppercase'

    class Meta:
        model = lace_models.Contacto
        fields = "__all__"
        widgets = {
            'id_empresa': forms.Select(attrs={'class': 'select-item'}),
        }

class SiteCollectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if not 'Checkbox' in str(visible.field.widget):
                visible.field.widget.attrs['style'] = 'text-transform:uppercase'

    class Meta:
        model = lace_models.Sitio
        fields = (
            'id_empresa',
            'telefono',
            'email',
            'calle',
            'noint',
            'noext',
            'codigopostal',
            'colonia',
            'alcaldia_municipio',
            'entidadfed',
            'pais',
        )
        widgets = {
            'id_empresa': forms.Select(attrs={'class': 'select-item'}),
        }


class InstrumentsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        parent = kwargs.pop("parent", None)
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if not 'Checkbox' in str(visible.field.widget):
                visible.field.widget.attrs['style'] = 'text-transform:uppercase'
        if parent:
            self.fields['id_sitio'].queryset = lace_models.Sitio.objects.filter(id_empresa= parent)

    class Meta:
        model = lace_models.Instrumento
        fields = (
            'id_empresa',
            'clave_id',
            'areamagnitud',
            'marca',
            'modelo',
            'serie',
            'intervalooperacion',
            'alcance',
            'exactitud',
            'emt',
            'divisionminima',
            'puntoscalibracion',
            'id_sitio',
        )
        widgets = {
            'id_empresa': forms.Select(attrs={'class': 'select-item'}),
            'id_sitio': forms.Select(attrs={'class': 'select-item'}),
            'areamagnitud': forms.SelectMultiple
        }


#---------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------- Formularios para crear Orden de Servicio -------------------------------------------------
#---------------------------------------------------- Test 1 ---------------------------------------------------------------------
class OrdenServicioFormulario1(forms.ModelForm):
    class Meta:
        model = lace_models.OrdenServicio
        fields = {"id_cliente"}
        # widgets = 


class OrdenServicioFormulario2(forms.ModelForm):
    CHOICES_FIELDS = (
        (0, "-------------------"),
        (1, "Servicio en Sitio"),
        (2, "Recolección y Entrega"),
        (3, "Tercería (Subcontratación)"),
    )

    tipo_servicio = forms.ChoiceField(label= "opciones", choices= CHOICES_FIELDS)

    class Meta:
        model = lace_models.SubServicio
        fields = ['id_sitio', 'tipo_servicio']
        # fields = '__all__'
        # widgets = 


class OrdenServicioFormulario3(forms.ModelForm):
    class Meta:
        model = lace_models.SubServicio
        fields = {'id_instrumento'}
        # widgets = 


class OrdenServicioFormulario4(forms.ModelForm):
    class Meta:
        model = lace_models.InstrumentOS
        # fields = 
        exclude = {'id_OSSubServicio', 'id_instrumento'}
        # widgets = 


class OrdenServicioFormulario5(forms.ModelForm):
    class Meta:
        model = lace_models.SubServicio
        fields = {
            'id_facturacion',
            'id_certificado',
        }
        # widgets = 


class OrdenServicioFormulario6(forms.ModelForm):
    class Meta:
        model = lace_models.OrdenServicio
        fields = {
            'dia_servicio',
            'id_contacto',
            'observaciones_os',
        }
        widgets = {
            'dia_servicio': forms.DateTimeInput(attrs={"type": "datetime-local",  "class": "select-item"}),
        }

class ServicioSitioFormulario(forms.ModelForm):
    select_other = forms.ChoiceField(choices= ((1,''),), widget= forms.CheckboxSelectMultiple, label= "Otra Opción")
    class Meta:
        model = lace_models.ServicioSitio
        fields = {
            'epp',
            'epp_option',
            'select_other'
            }


class TerceriaFormulario(forms.ModelForm):
    class Meta:
        model = lace_models.TerceriaSubcontratacion
        fields = ['razonsocial']


class RecoleccionEntregaFormulario(forms.ModelForm):
    class Meta:
        model = lace_models.RecoleccionEntrega
        exclude = ['id_empresa', 'id_sitio']
#---------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------- Formularios para crear Orden de Servicio -------------------------------------------------
#---------------------------------------------------- Test 2 ---------------------------------------------------------------------
class OSFormulario1(forms.ModelForm):
    '''Formulario 1: los campos a llenar en este formulario pertenecen al modelo Orden de Servicio.
    se excluyen los campos "ID_status", "OrdenServicio" y "Día_registro" pues estos campos serán
    llenados automáticamente en el backend.'''

    class Meta:
        model = lace_models.OrdenServicio
        fields = ['id_cliente']
        widgets = {
            'dia_servicio': forms.DateTimeInput(attrs={"type": "datetime-local",  "class": "select-item"}),
        }

    def __init__(self, filter=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if filter != None:
            self.fields['id_cliente'].queryset = lace_models.ClienteEmpresa.objects.filter(id_empresa__contains= filter)

class OSFormulario2(forms.ModelForm):
    '''Formulario 2: los campos de este formulario pertenecen al modelo SubServicio.'''
    class Meta:
        model = lace_models.SubServicio
        exclude = ['id_ordenservicio']

# class OS