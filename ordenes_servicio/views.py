import json
import dateutil.parser as formatdate
from django.shortcuts import render
from django.urls import reverse
from ordenes_servicio import forms as form_app
from lace_app import models as models_app
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from formtools.wizard.views import SessionWizardView
from django.http import HttpResponse
# para generar PDF se necesita lo siguiente:
from django.template.loader import render_to_string, get_template
from weasyprint import HTML
from weasyprint.fonts import FontConfiguration
import django.views.generic as views
from lace_app.models import(
    InstrumentosImagen,
    OrdenServicio,
    Facturacion,
)
from alta_data import forms as ad_forms
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------- Orden de Servicio ----------------------------------------------------------
#--------------------------------------------------------- Lista ---------------------------------------------------------------
class ServiceOrderList(ListView):
    model = OrdenServicio
    template_name = 'ordenes_servicio/service_order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ordenes'] = OrdenServicio.objects.all()

        return context
#-------------------------------------------------------- Creación -------------------------------------------------------------
#---------------------------------------------------- Test 2 ---------------------------------------------------------------------
class ServiceOrderCreateView(views.FormView):
    # template_name = "../templates/ordenes_servicio/old_service_order_create.html"
    template_name = "../templates/ordenes_servicio/service_order_create.html"
    form_class = form_app.OSFormulario1
    form_list = [
        [[form_class,form_app.OSFormulario9], form_app.OSFormulario2, form_app.OSFormulario3, form_app.OSFormulario4, form_app.OSFormulario5],
        [form_app.OSFormulario6],[[form_app.OSFormulario7, form_app.OSFormulario8]],[form_app.OSFormulario9],
        ]
    paso = None
    sub_paso = None
    success_url = reverse_lazy('ordenes_servicio:orden_servicio_list')

    def post(self, request, *args, **kwargs):
        """Controla el flujo del código según las peticiones en el objeto 'request'"""
        if request.POST.get("servicio") == "detalles":
            objeto = self.get_objects(request)
            return HttpResponse(objeto)
        elif request.POST.get("servicio") == "formulario":
            formulario = self.get_forms(request)
            return HttpResponse(formulario)
        elif request.POST.get("servicio") == "crear":
            request_crear = self.create_object(request)
            return HttpResponse(request_crear)
        elif request.POST.get("servicio") == "actualizar":
            if request.POST.get("valor"):
                request_actualizar = self.update_object(request)
            else:
                request_actualizar = self.update_db(request)
            return HttpResponse(request_actualizar)
        else:
            flow_control = self.step_checker(request)
            if flow_control.get('ajax'):
                context = self.get_context_data(form= self.form_list)
                return HttpResponse(json.dumps(context))
            else:
                return super().post(request)

    def get(self, request, *args, **kwargs):
        self.step_checker(request)

        if self.paso == 1:
            context = self.get_context_data(form= self.form_list)

        return render(request, self.template_name, context= context)

    def get_context_data(self, form, **kwargs):
        context = super().get_context_data(**kwargs)
        new_context = {}
        new_context['paso'] = self.paso
        new_context['sub_paso'] = self.sub_paso
        new_context['id_parent'] = self.request.POST.get('id_parent')

        if self.paso == 1:
            if self.sub_paso == 1:
                print(self.forms_dict())
                new_context['form_list'] = self.forms_dict()
            if self.sub_paso == 2:
                form = self.forms_dict()
                new_context['html'] = self.formatting(
                    render_to_string(
                        '../templates/ordenes_servicio/OSForms_templates/form_2.html', context= form
                        ))
                new_context['html_extra'] = self.formatting(
                    render_to_string(
                        '../templates/ordenes_servicio/OSForms_templates/form_5.html', context= form
                    ))
            if self.sub_paso == 3:
                form = self.forms_dict()
                new_context['html'] = self.formatting(
                    render_to_string(
                        '../templates/ordenes_servicio/OSForms_templates/form_2.html', context= form
                        ))
        elif self.paso == 2:
            form = self.forms_dict()
            parent = self.request.POST.get('id_empresa')
            instrument_list = models_app.Instrumento.objects.filter(id_empresa= int(parent))
            html_name = form.get('SubservicioForm2').fields['id_instrumento'].widget.attrs['id']
            name_list = "listado_" + str(self.request.POST.get("id_parent"))
            id_table = "instrument_table_" + html_name.split("_")[-1]
            html_list = {}
            html_list['certificado'] = self.formatting(
                render_to_string(
                    '../templates/ordenes_servicio/OSForms_templates/form_3.html', context= {"form": form, "list": name_list, "control": "certificado"}
                ))
            html_list['facturacion'] = self.formatting(
                render_to_string(
                    '../templates/ordenes_servicio/OSForms_templates/form_3.html', context= {"form": form, "list": name_list, "control": "facturacion"}
                ))
            html_list['instrumentos'] = self.formatting(
                render_to_string(
                    '../templates/ordenes_servicio/OSForms_templates/form_3.html', context= {"form": form, "list": name_list, "control": "instrumento", "html_name": html_name}
                ))
            html_list['lista_instrumentos'] = self.formatting(
                render_to_string(
                    '../templates/ordenes_servicio/OSForms_templates/form_3.html', context= {"id": html_name, "list": name_list, "object_list": instrument_list, "control": "instrumento_lista", "html_name": html_name[3:], "id_table": id_table}
                ))
            html_list['id_table'] = id_table
            new_context['html'] = html_list

        elif self.paso == 3:
            form = self.forms_dict()
            new_context['instrument'] = self.request.POST.get('posicion')
            new_context['html'] = self.formatting(
                render_to_string(
                    '../templates/ordenes_servicio/OSForms_templates/form_4.html', context= form
                )
            )
        elif self.paso == 4:
            form = self.forms_dict()
            new_context['html'] = self.formatting(
                render_to_string(
                    '../templates/ordenes_servicio/OSForms_templates/form_5.html', context = form
                )
            )
        return new_context

    def form_valid(self, form):
        print(self.request.POST)
        meta_data = self.request.POST

        if form.is_valid():
            sub_servicios = int(meta_data.get("sub_servicios_total"))
            sub_serv_list = []
            #Campos necesarios para crear objeto OrdenServicio
            obj_os = self.ordenServicioObjeto(meta_data)
            #Campos necesarios para crear objeto SubServicio
            for sub_servicio in range(sub_servicios):
                obj_subserv = self.subServicioObjeto(meta_data, sub_servicio)
                sub_serv_list.append(obj_subserv)
                #Campos necesarios para crear objeto InstrumentOS
                instrumentos = int(len(meta_data.get("id_instrumento_{}".format(sub_servicio)))/2);
                obj_instrumentOS = []
                for item in range(instrumentos):

                    obj_instrumentOS.append(self.instrumentOSObjeto(meta_data, obj_subserv, sub_servicio, item))
                    #Campos necesarios para crear objeto Fotografia
                    total_img = int(meta_data.get("TOTAL_images_{}_{}".format(sub_servicio, item)))
                    obj_foto = []
                    for img in range(total_img):
                        obj_foto.append(self.fotografiaObjeto(sub_servicio, item, img))
                    #Adjuntando fotografías
                    for foto in obj_foto:
                        obj_instrumentOS[-1].id_imagen.add(foto)
                #Campos necesarios para crear objeto ServicioSitio
                obj_sitio = self.tipoSitioObjeto(meta_data, obj_os, sub_servicio)
                #Agregando subservicios a OS
                for subserv in sub_serv_list:
                    obj_os.id_subservicio.add(subserv)

        return HttpResponse(json.dumps({"status": 248, "url": self.get_success_url()}))
    
    def ordenServicioObjeto(self, meta_data):
        #Campos necesarios para crear objeto OrdenServicio
        id_cliente = meta_data.get('id_cliente')
        # servicioContratado = meta_data.get('servicioContratado')
        id_contacto = meta_data.get('id_contacto')
        dia_servicio = meta_data.get('dia_servicio')
        observaciones_os = meta_data.get('observaciones_os')
        
        cliente = models_app.ClienteEmpresa.objects.get(id= int(id_cliente))
        contacto = models_app.Contacto.objects.get(id= int(id_contacto))
        estatus = models_app.Estatus.objects.get(id= 1)
        # servicio = models_app.tipoServicio.objects.get(id= int(servicioContratado))
        dia_servicio = formatdate.isoparse(dia_servicio)

        obj_os = models_app.OrdenServicio.objects.create(
            dia_servicio= dia_servicio,
            observaciones_os= observaciones_os,
            id_cliente= cliente,
            id_contacto= contacto,
            estatus= estatus,
            # servicioContratado= servicio
        )

        obj_os.id_orden = "OS-0000-{}".format(str(obj_os.id))
        obj_os.no_certificado = "CE-0000-{}".format(str(obj_os.id))
        obj_os.save()

        return obj_os

    def subServicioObjeto(self, meta_data, parent):
        #Campos necesarios para crear objeto SubServicio
        id_facturacion = meta_data.get('facturacion_{}'.format(parent))
        id_certificado = meta_data.get('certificado_{}'.format(parent))
        id_sitio = meta_data.get('sitio_{}'.format(parent))
        id_instrumento = meta_data.get('id_instrumento_{}'.format(parent))
        id_servicioContratado = meta_data.get('servicioContratado_{}'.format(parent))

        facturacion = models_app.Facturacion.objects.get(id= int(id_facturacion))
        certificado = models_app.Certificado.objects.get(id= int(id_certificado))
        sitio = models_app.Sitio.objects.get(id= int(id_sitio))
        servicioContratado = models_app.tipoServicio.objects.get(id= int(id_servicioContratado))
        
        instrumento = []
        for item in id_instrumento:
            instrumento.append(models_app.Instrumento.objects.get(id= int(item)))

        obj_subserv = models_app.SubServicio(
            id_facturacion= facturacion,
            id_sitio= sitio,
            id_certificado= certificado,
            servicioContratado= servicioContratado,
        )
        obj_subserv.save()

        for item in instrumento:
            obj_subserv.id_instrumento.add(item)
        
        return obj_subserv

    def instrumentOSObjeto(self, meta_data, id_subservicio, sub_servicio, item):
        #Campos necesarios para crear objeto InstrumentOS
        id_instrumento = meta_data.get('id_instrumento_{}'.format(sub_servicio))
        id_servicio = meta_data.get('servicio_{}_{}'.format(sub_servicio, item))
        servicio = []
        id_vigencia = meta_data.get('vigencia_{}_{}'.format(sub_servicio, item))
        observaciones_ios = meta_data.get('observaciones_ios_{}_{}'.format(sub_servicio, item))

        id_instrumento = models_app.Instrumento.objects.get(id= int(id_instrumento))
        for item in id_servicio:
            servicio.append(models_app.ServicioInstrumento.objects.get(id= int(item)))

        id_vigencia = models_app.Vigencia.objects.get(id= int(id_vigencia))

        instrumentoObjeto = models_app.InstrumentOS(
            id_instrumento= id_instrumento,
            id_vigencia= id_vigencia,
            observaciones_ios= observaciones_ios,
            id_OSSubServicio= id_subservicio
        )
        instrumentoObjeto.save()

        for item in id_servicio:
            instrumentoObjeto.id_servicio.add(item)
        #Falta agregar imagenes ManytoMany
        return instrumentoObjeto

    def tipoSitioObjeto(self, meta_data, os, sub_servicio):
        tipoServ = meta_data.get('servicioContratado_{}'.format(sub_servicio))
        id_sitio = meta_data.get('sitio_{}'.format(sub_servicio))
        id_empresa = meta_data.get('id_cliente')

        sitio = models_app.Sitio.objects.get(id= int(id_sitio))
        empresa = models_app.ClienteEmpresa.objects.get(id= int(id_empresa))

        if tipoServ == "1":
            obj_sitio = models_app.ServicioSitio(
                id_sitio= sitio,
                id_empresa= empresa,
                epp_option= str(os.id)
                )
            obj_sitio.save()

            #Campos necesarios para crear objeto ServicioSitio
            epp = meta_data.get('epp_{}'.format(sub_servicio))
            epp_id = []
            for item in epp:
                epp_id.append(models_app.EPP.objects.get(id= int(item)))

            for item in epp_id:
                obj_sitio.epp.add(item)

        elif tipoServ == "2":
            #Campos necesarios para crear objeto RecoleccionEntrega
            atencion = meta_data.get('atencion_{}'.format(sub_servicio))
            observaciones_re = meta_data.get('observaciones_re_{}'.format(sub_servicio))
            recoleccion = meta_data.get('recoleccion_{}'.format(sub_servicio))
            entrega = meta_data.get('entrega_{}'.format(sub_servicio))

            if recoleccion == "on":
                recoleccion = True
            else:
                recoleccion = False

            if entrega == "on":
                entrega = True
            else:
                entrega = False

            obj_sitio = models_app.RecoleccionEntrega(
                atencion= atencion,
                observaciones_re= observaciones_re,
                recoleccion= recoleccion,
                entrega= entrega,
                id_sitio= sitio,
                id_empresa= empresa
            )

            obj_sitio.save()

        elif tipoServ == "3":
            #Campos necesarios para crear objeto TerceriaSubcontratacion
            razonsocial = meta_data.get('razonsocial_{}'.format(sub_servicio))
            obj_sitio = models_app.TerceriaSubcontratacion(
                razonsocial= razonsocial,
                id_sitio= sitio,
                id_empresa= empresa
            )
            obj_sitio.save()
        
        return obj_sitio

    def fotografiaObjeto(self, sub_servicio, instrumento, num_img):
        img = self.request.FILES.get("imagen_{}_{}_{}"\
            .format(sub_servicio, instrumento, num_img))
        foto = models_app.Fotografia(imagen = img)
        foto.save()

        return foto

    def step_checker(self, request):
        ajax = False
        submit = False

        if 'GET' in request.method:
            self.paso = 1
            self.sub_paso = 1
        else:
            if request.POST.get('AJAXCall') == "1":
                ajax = True
                if request.POST.get('submit') == "next":
                    paso = request.POST.get('paso')
                    self.paso = int(paso) + 1
                    self.sub_paso = 1
                else:
                    self.paso = int(request.POST.get('paso'))
                    self.sub_paso = int(request.POST.get('sub_paso')) + 1
            else:
                submit = True

        return {'submit': submit, 'ajax': ajax}

    def forms_dict(self):
        dict_keys = [
            [['OrdenServicioForm','DatosExtraForm'], 'SubServicioForm', 'servicioContratado', 'recoleccionEntrega', 'terceria'],
            ['SubservicioForm2'],['InstrumentOSForm'],['OrdenServicioForm2']
                        ]
        dict_form = {}
        i = self.paso - 1
        j = self.sub_paso - 1
        if j == 2:
            servicioC = int(self.request.POST.get('servicioContratado'))
            if servicioC == 1:
                j = 2
            elif servicioC == 2:
                j = 3
            else:
                j = 4

        key = dict_keys[i][j]
        form = self.form_list[i][j]

        if self.paso == 1:
            if self.sub_paso == 1:
                    dict_form[key[0]] = form[0](**self.get_form_kwargs())
            elif self.sub_paso == 2:
                filter = self.request.POST.get('id_empresa')
                parent = self.request.POST.get('id_parent')
                dict_form[key] = form(filter= filter, parent= parent, **self.get_form_kwargs())
                dict_form['DatosExtraForm'] = form_app.OSFormulario9(filter= filter, **self.get_form_kwargs())
            elif self.sub_paso == 3:
                parent = self.request.POST.get('id_parent')
                dict_form[key] = form(parent= parent, **self.get_form_kwargs())
        elif self.paso == 2:
            parent = self.request.POST.get('id_parent')
            cliente = self.request.POST.get('id_empresa')
            sitio = self.request.POST.get('sitio_' + parent)
            filter = {'cliente': cliente, 'sitio': sitio}

            dict_form[key] = form(filter = filter, parent= parent, **self.get_form_kwargs())
        elif self.paso == 3:
            parent = self.request.POST.get('id_parent')
            instrument = self.request.POST.get('posicion')
            dict_form[key] = [formulario(parent= parent, instrument= instrument, **self.get_form_kwargs()) for formulario in form]
        elif self.paso == 4:
            dict_form[key] = form(**self.get_form_kwargs())

        return dict_form

    def formatting(self, plantillaTexto):
        return plantillaTexto.replace("\n","")
    
    def get_objects(self, request):
        parent = request.POST.get("elemento")
        id = request.POST.get("valor")

        if "cliente" in parent:
            objeto = models_app.ClienteEmpresa.objects.get(id= int(id))
            template = self.formatting(render_to_string(
                "../templates/ordenes_servicio/detalles_mini/cliente_detalles.html",
                context= {"object": objeto, "opcion": "cliente"}))
        elif "contacto" in parent:
            objeto = models_app.Contacto.objects.get(id= int(id))
            template = self.formatting(render_to_string(
                "../templates/ordenes_servicio/detalles_mini/cliente_detalles.html",
                context= {"object": objeto, "opcion": "contacto"}))
        elif "sitio" in parent:
            objeto = models_app.Sitio.objects.get(id= int(id))
            template = self.formatting(render_to_string(
                "../templates/ordenes_servicio/detalles_mini/cliente_detalles.html",
                context= {"object": objeto, "opcion": "sitio"}))
        elif "certificado" in parent:
            objeto = models_app.Certificado.objects.get(id= int(id))
            template = self.formatting(render_to_string(
                "../templates/ordenes_servicio/detalles_mini/cliente_detalles.html",
                context= {"object": objeto, "opcion": "certificado"}))
        elif "facturacion" in parent:
            objeto = models_app.Facturacion.objects.get(id= int(id))
            template = self.formatting(render_to_string(
                "../templates/ordenes_servicio/detalles_mini/cliente_detalles.html",
                context= {"object": objeto, "opcion": "facturacion"}))
        elif "instrumento" in parent:
            objeto = models_app.Instrumento.objects.get(id= int(id))
            template = self.formatting(render_to_string(
                "../templates/ordenes_servicio/detalles_mini/cliente_detalles.html",
                context= {"object": objeto, "opcion": "instrumento"}))
        
        dict_object = {"model": template, "parent": parent, "accion": "detalles"}
        dict_object = json.dumps(dict_object)

        return dict_object

    def get_forms(self, request):
        parent = request.POST.get("elemento")
        if "cliente" in parent:
            formulario = ad_forms.ClientsForm(**self.get_form_kwargs())
            template = self.formatting(render_to_string(
                "../templates/ordenes_servicio/create_objects_mini/cliente_crear.html",
                context= {"form": formulario}))
        elif "contacto" in parent:
            formulario = ad_forms.ContactProfieForm(**self.get_form_kwargs())
            template = self.formatting(render_to_string(
                "../templates/ordenes_servicio/create_objects_mini/contacto_crear.html",
                context= {"form": formulario}))
        elif "sitio" in parent:
            formulario = ad_forms.SiteCollectForm(**self.get_form_kwargs())
            template = self.formatting(render_to_string(
                "../templates/ordenes_servicio/create_objects_mini/sitio_crear.html",
                context= {"form": formulario}))
        elif "certificado" in parent:
            formulario = ad_forms.CertificateForm(**self.get_form_kwargs())
            template = self.formatting(render_to_string(
                "../templates/ordenes_servicio/create_objects_mini/certificado_crear.html",
                context= {"form": formulario}))
        elif "facturacion" in parent:
            formulario = ad_forms.BillingForm(**self.get_form_kwargs())
            template = self.formatting(render_to_string(
                "../templates/ordenes_servicio/create_objects_mini/facturacion_crear.html",
                context= {"form": formulario}))
        elif "instrumento" in parent:
            id_parent = request.POST.get('valor')
            print("Imprimiendo valor request: ", request.POST)
            print("Imprimiendo valor id_parent: ", id_parent)
            formulario = ad_forms.InstrumentsForm(**self.get_form_kwargs(), parent= id_parent)
            template = self.formatting(render_to_string(
                "../templates/ordenes_servicio/create_objects_mini/instrumento_crear.html",
                context= {"form": formulario}))
        
        dict_object = {"model": template, "parent": parent, "accion": "crear"}
        dict_object = json.dumps(dict_object)

        return dict_object

    def create_object(self, request):
        parent = request.POST.get("elemento")
        form = json.loads(request.POST.get("form"))

        if "cliente" in parent:
            formulario = ad_forms.ClientsForm(form)
        elif "contacto" in parent:
            formulario = ad_forms.ContactProfieForm(form)
        elif "sitio" in parent:
            formulario = ad_forms.SiteCollectForm(form)
        elif "certificado" in parent:
            formulario = ad_forms.CertificateForm(form)
        elif "facturacion" in parent:
            formulario = ad_forms.BillingForm(form)
        elif "instrumento" in parent:
            areamagnitud = []
            for index in request.POST.get("areamagnitud").split(","):
                areamagnitud.append(index)
            form["areamagnitud"] = areamagnitud
            formulario = ad_forms.InstrumentsForm(form)

        object_created = formulario.save()
        id = object_created.id
        option = object_created.__str__()
        if "instrumento" in parent:
            id = parent.split("_")[-1]
            html_name = parent
            instrument_list = models_app.Instrumento.objects.filter(id_empresa= int(form["id_empresa"]))
            name_list = "listado_" + id
            id_table = "instrument_table_" + id

            html_table = self.formatting(
                render_to_string(
                    '../templates/ordenes_servicio/OSForms_templates/form_3.html', context= {"id": html_name, "list": name_list, "object_list": instrument_list, "control": "instrumento_lista", "html_name": html_name[3:], "id_table": id_table}
                ))
            parent = "id_paso_3_instrumento_" + id
            dict_object = {"accion": "actualizar_elemento", "parent": parent, "model": {"html": html_table, "id_table": id_table}}
        else:
            dict_object = {"accion": "actualizar_elemento", "parent": parent, "model": {"option": option, "value": id}}
        dict_object = json.dumps(dict_object)

        return dict_object
    
    def update_object(self, request):
        parent = request.POST.get("elemento")
        valor_id = request.POST.get("valor")

        if "cliente" in parent:
            model = models_app.ClienteEmpresa
            instance = get_object_or_404(model, id= int(valor_id))
            formulario = ad_forms.ClientsForm(instance= instance)
            template = self.formatting(render_to_string(
                "../templates/ordenes_servicio/create_objects_mini/cliente_crear.html",
                context= {"form": formulario}))
        elif "contacto" in parent:
            model = models_app.Contacto
            instance = get_object_or_404(model, id= int(valor_id))
            formulario = ad_forms.ContactProfieForm(instance= instance)
            template = self.formatting(render_to_string(
                "../templates/ordenes_servicio/create_objects_mini/contacto_crear.html",
                context= {"form": formulario}))
        elif "sitio" in parent:
            model = models_app.Sitio
            instance = get_object_or_404(model, id= int(valor_id))
            formulario = ad_forms.SiteCollectForm(instance= instance)
            template = self.formatting(render_to_string(
                "../templates/ordenes_servicio/create_objects_mini/sitio_crear.html",
                context= {"form": formulario}))
        elif "certificado" in parent:
            model = models_app.Certificado
            instance = get_object_or_404(model, id= int(valor_id))
            formulario = ad_forms.CertificateForm(instance= instance)
            template = self.formatting(render_to_string(
                "../templates/ordenes_servicio/create_objects_mini/certificado_crear.html",
                context= {"form": formulario}))
        elif "facturacion" in parent:
            model = models_app.Facturacion
            instance = get_object_or_404(model, id= int(valor_id))
            formulario = ad_forms.BillingForm(instance= instance)
            template = self.formatting(render_to_string(
                "../templates/ordenes_servicio/create_objects_mini/facturacion_crear.html",
                context= {"form": formulario}))
        
        dict_object = {"model": template, "parent": parent, "accion": "actualizar"}
        dict_object = json.dumps(dict_object)

        return dict_object

    def update_db(self, request):
        parent = request.POST.get("elemento")
        valor_id = request.POST.get("elemento_valor")
        form = json.loads(request.POST.get("form"))

        if "cliente" in parent:
            model = models_app.ClienteEmpresa.objects.get(id= int(valor_id))
        elif "contacto" in parent:
            model = models_app.Contacto.objects.get(id= int(valor_id))
        elif "sitio" in parent:
            model = models_app.Sitio.objects.get(id= int(valor_id))
        elif "certificado" in parent:
            model = models_app.Certificado.objects.get(id= int(valor_id))
        elif "facturacion" in parent:
            model = models_app.Facturacion.objects.get(id= int(valor_id))
        
        for key, value in form.items():
            if key != "id_empresa":
                setattr(model, key, value)
            else:
                if not("cliente" in parent):
                    value = models_app.ClienteEmpresa.objects.get(id= int(value))
                setattr(model,key,value)

        model.save()

        id = model.id
        option = model.__str__()
        dict_object = {"accion": "actualizar_elemento", "parent": parent, "model": {"option": option, "value": id}}
        dict_object = json.dumps(dict_object)

        return dict_object

#----------------------------------------------------- Actualización -------------------------------------------------------------
# class ServiceOrderUpdateView(SessionWizardView):
#-------------------------------------------------------- Detalles ---------------------------------------------------------------
class ServiceOrderDetailView(DetailView):
    template_name = "../templates/ordenes_servicio/service_order_detail.html"
    model = models_app.OrdenServicio

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date = context['object'].dia_servicio
        date = str(date)[:-9].replace(" ", "T")
        context['new_format'] = date
        print(context)
        return context

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(self.model, id= id_)
#-------------------------------------------------------- Eliminar ---------------------------------------------------------------

#--------------------------------------------------------- PDF -----------------------------------------------------------------
def export_pdf(request, **kwargs):
    id_n = kwargs.get('id')
    #facturacion = BillingData.objects.filter(rfc_data__in=['DML7905239C4'])
    orden_servicio = OrdenServicio.objects.get(id=id_n)

    context = {
        'orden': orden_servicio,
    }
    html = render_to_string("ordenes_servicio/OS_PDF.html", context)

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "inline; report.pdf"

    font_config = FontConfiguration()
    HTML(string=html, base_url=request.build_absolute_uri()
         ).write_pdf(response, font_config=font_config)

    return response
