from django import forms
from weasyprint.css.computed_values import length
from lace_app import models as lace_models
from datetime import date, timedelta
#------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------- Formularios para Orden de Servicio ------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------
class OrdenServicioForm1(forms.ModelForm):
    """Primer paso para la creación de una orden de servicio. Aquí es donde se define
    los servicios que se aplicarán a los instrumentos."""
    hidden_field = forms.CharField(max_length= 255, required= False, widget= forms.HiddenInput(attrs= {'name':'id_sub_service'}))

    class Meta:
        model = lace_models.SubServicio
        fields = '__all__'

        widgets = {
            'id_instrumento': forms.CheckboxSelectMultiple,
            'id_sitio': forms.Select,
            'id_certificado': forms.Select,
        }


class OrdenServicioForm2(forms.ModelForm):
    """Segundo paso para la creación de una orden de servicio. Aquí es donde se relacionan
    los instrumentos con el sitio al que pertenecen."""

    class Meta:
        model = lace_models.OrdenServicio
        exclude = ("id_subservicio", "estatus", "id_orden", "no_certificado")
        widgets = {
            'id_facturacion': forms.Select,
            'dia_servicio': forms.DateTimeInput(attrs={"type": "datetime-local"}),
            'observaciones': forms.Textarea,
        }
#---------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------- Formularios para crear Orden de Servicio -------------------------------------------------
#---------------------------------------------------- Test 2 ---------------------------------------------------------------------

class OSFormulario1(forms.ModelForm):
    """Formulario 1: los campos a llenar en este formulario pertenecen al modelo Orden de Servicio.
    se excluyen los campos "ID_status", "OrdenServicio" y "Día_registro" pues estos campos serán
    llenados automáticamente en el backend."""
    # def __init__(self, filter=None, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    class Meta:
        model = lace_models.OrdenServicio
        fields = ['id_cliente']
        # widgets = {
        #     'servicioContratado': forms.Select(attrs={"disabled": True}),
        # }


class OSFormulario2(forms.ModelForm):
    """Formulario 2: los campos de este formulario pertenecen al modelo SubServicio."""
    def __init__(self, filter=None, parent="0", *args, **kwargs):
        super().__init__(*args, **kwargs)
        if filter != None:
            self.fields['id_sitio'].queryset = lace_models.Sitio.objects.filter(id_empresa= filter)

        self.fields['id_sitio'].widget.attrs.update({"id": "id_sitio_" + parent})
        self.fields['servicioContratado'].widget.attrs.update({"id": "id_servicioContratado_" + parent})
        self.fields['servicioContratado'].widget.attrs['class'] = "js_class_2"
        self.custom_names = {'id_sitio': "sitio_" + parent, "servicioContratado": "servicioContratado_" + parent}

    def get_custom_names(self):
        return self.custom_names

    def add_prefix(self, field_name):
        customs_names = self.get_custom_names()
        field_name = self.custom_names.get(field_name, field_name)
        return super().add_prefix(field_name)

    class Meta:
        model = lace_models.SubServicio
        fields = ['id_sitio', 'servicioContratado']


class OSFormulario3(forms.ModelForm):
    """Formulario 3: los campos de este formulario pertenecen al modelo SubServicio."""
    def __init__(self, parent="0", *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['epp'].widget.attrs.update({"id": "id_epp_" + parent})
        self.custom_names = {'epp': "epp_" + parent}

    def get_custom_names(self):
        return self.custom_names

    def add_prefix(self, field_name):
        customs_names = self.get_custom_names()
        field_name = self.custom_names.get(field_name, field_name)
        return super().add_prefix(field_name)

    class Meta:
        model = lace_models.ServicioSitio
        fields = ['epp']


class OSFormulario4(forms.ModelForm):
    """Formulario 4: los campos de este formulario pertenecen al modelo SubServicio."""
    def __init__(self, parent="0", *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['atencion'].widget.attrs.update({"id": "id_atencion_" + parent})
        self.fields['observaciones_re'].widget.attrs.update({"id": "id_observaciones_re_" + parent})
        self.fields['recoleccion'].widget.attrs.update({"id": "id_recoleccion_" + parent})
        self.fields['entrega'].widget.attrs.update({"id": "id_entrega_" + parent})
        self.custom_names = {"atencion": "atencion_" + parent, "observaciones_re": "observaciones_re_" + parent,\
                             "recoleccion": "recoleccion_" + parent, "entrega": "entrega_" + parent}

    def get_custom_names(self):
        return self.custom_names

    def add_prefix(self, field_name):
        customs_names = self.get_custom_names()
        field_name = self.custom_names.get(field_name, field_name)
        return super().add_prefix(field_name)

    class Meta:
        model = lace_models.RecoleccionEntrega
        exclude = ['id_sitio', 'id_empresa']


class OSFormulario5(forms.ModelForm):
    """Formulario 2: los campos de este formulario pertenecen al modelo SubServicio."""
    def __init__(self, parent="0", *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['razonsocial'].widget.attrs.update({"id": "id_razonsocial_" + parent})
        self.custom_names = {"razonsocial": "razonsocial_" + parent}

    def get_custom_names(self):
        return self.custom_names

    def add_prefix(self, field_name):
        customs_names = self.get_custom_names()
        field_name = self.custom_names.get(field_name, field_name)
        return super().add_prefix(field_name)

    class Meta:
        model = lace_models.TerceriaSubcontratacion
        exclude = ['id_sitio', 'id_empresa']


class OSFormulario6(forms.ModelForm):
    """Formulario 6: los campos de este formulario pertenecen al modelo SubServicio."""
    def __init__(self, filter=None, parent="0", *args, **kwargs):
        super().__init__(*args, **kwargs)

        if filter != None:
            cliente = filter.get('cliente')
            sitio = filter.get('sitio')
            self.fields['id_certificado'].queryset = lace_models.Certificado.objects.filter(id_empresa= cliente)
            self.fields['id_facturacion'].queryset = lace_models.Facturacion.objects.filter(id_empresa= cliente)
            self.fields['id_instrumento'].queryset = lace_models.Instrumento.objects.filter(id_empresa= cliente, id_sitio= sitio)

        self.fields['id_certificado'].widget.attrs.update({"id": "id_certificado_" + parent})
        self.fields['id_facturacion'].widget.attrs.update({"id": "id_facturacion_" + parent})
        self.fields['id_instrumento'].widget.attrs.update({"id": "id_instrumento_" + parent})
        
        self.custom_names = {
            "id_certificado": "certificado_" + parent,
            "id_facturacion": "facturacion_" + parent,
            "id_instrumento": "instrumento_" + parent
            }

    def get_custom_names(self):
        return self.custom_names

    def add_prefix(self, field_name):
        customs_names = self.get_custom_names()
        field_name = self.custom_names.get(field_name, field_name)
        return super().add_prefix(field_name)

    class Meta:
        model = lace_models.SubServicio
        fields = ['id_certificado', 'id_facturacion', 'id_instrumento']
        widgets = {
            'id_instrumento': forms.CheckboxSelectMultiple,
        }


class OSFormulario7(forms.ModelForm):
    """Formulario 7: Contiene campos adjuntos al instrumento seleccionado (Fotografías, Vigencia, Servicio)."""
    def __init__(self, parent= "0", instrument= "0", *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['id_servicio'].widget.attrs.update({"id": "id_servicio_{}_{}".format(parent, instrument)})
        self.fields['id_vigencia'].widget.attrs.update({"id": "id_vigencia_{}_{}".format(parent, instrument)})
        self.fields['observaciones_ios'].widget.attrs.update({"id": "id_observaciones_ios_{}_{}".format(parent, instrument)})
        
        self.custom_names = {
            "id_servicio": "servicio_{}_{}".format(parent, instrument),
            "id_vigencia": "vigencia_{}_{}".format(parent, instrument),
            "observaciones_ios": "observaciones_ios_{}_{}".format(parent, instrument)
            }

    
    def get_custom_names(self):
        return self.custom_names

    def add_prefix(self, field_name):
        customs_names = self.get_custom_names()
        field_name = self.custom_names.get(field_name, field_name)
        return super().add_prefix(field_name)
    
    class Meta:
        model = lace_models.InstrumentOS
        fields = ['id_servicio', 'id_vigencia', 'observaciones_ios']
        widgets = {
            'observaciones_ios': forms.Textarea,
        }


class OSFormulario8(forms.ModelForm):
    """Formulario 8: Contiene campos adjuntos al instrumento seleccionado (Fotografía)."""
    def __init__(self, parent= "0", instrument= "0", *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['imagen'].widget.attrs.update({"id": "id_imagen_{}_{}_0".format(parent, instrument)})
        self.fields['imagen'].widget.attrs.update({"class": "show-for-sr"})

        self.fields['images_hide'].widget.attrs.update({"id": "id_TOTAL_images_{}_{}".format(parent, instrument)})
        self.fields['images_hide'].widget.attrs.update({"value": 1})
        
        self.custom_names = {
            "imagen": "imagen_{}_{}_0".format(parent, instrument),
            "images_hide": "TOTAL_images_{}_{}".format(parent, instrument)
            }

    def get_custom_names(self):
        return self.custom_names

    def get_hide_attrs(self):
        return self.image_attrs

    def add_prefix(self, field_name):
        customs_names = self.get_custom_names()
        field_name = self.custom_names.get(field_name, field_name)
        return super().add_prefix(field_name)

    images_hide = forms.CharField(widget= forms.HiddenInput())
    class Meta:
        model = lace_models.Fotografia
        fields = ['imagen']


class OSFormulario9(forms.ModelForm):
    """Formulario 9: Contiene campos para completar la Orden de Servicio."""
    def __init__(self, filter= 0, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if filter != None:
            self.fields['id_contacto'].queryset = lace_models.Contacto.objects.filter(id_empresa= filter)

    class Meta:
        model = lace_models.OrdenServicio
        fields = ['id_contacto', 'dia_servicio', 'observaciones_os']
        
        current_day = date.today()
        max_day = current_day + timedelta(30)
        current_day = str(current_day) + "T00:00"
        max_day = str(max_day) + "T00:00"

        widgets = {
            'dia_servicio': forms.DateTimeInput(attrs={"type": "datetime-local", "min":current_day}),
            'observaciones_os': forms.Textarea,
        }


