import json
from django.shortcuts import get_object_or_404, render, redirect
from formtools.wizard.views import SessionWizardView
# from django.core.cache import cache
from django.forms import formset_factory
from django.forms import model_to_dict
from lace_app import models as models_app
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
import django.views.generic as views
from alta_data import forms as form_app
from lace_app.models import(
    
    ClienteEmpresa,
    Certificado,
    Facturacion,
    Contacto,
    Sitio,
    Instrumento,
)

from .forms import (
    ClientsForm,
    CertificateForm,
    BillingForm,
    ContactProfieForm,
    SiteCollectForm,
    InstrumentsForm
)

def upper_fields(query, query_object):
    for field in query.model._meta.fields:
        name = field.name
        try:
            val = getattr(query_object, name, False)
            if val:
                if name == 'no_int' and val.lower() == 's/n':
                    setattr(query_object, name, '')
                else:
                    setattr(query_object, name, val.upper())
        except AttributeError:
            pass

    return query_object

#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------#---------------------------------------- FACTURACIÓN ------------------------------------------------------
#------------------------------------- CRUD Clientes ------------------------------------------------------

class ClientsList(views.ListView):
    model = ClienteEmpresa
    template_name = 'alta_data/clients.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cliente'] = ClienteEmpresa.objects.all()
        return context

class ClientsDetail(views.DetailView):
    template_name = 'alta_data/clients_detail.html'
    queryset = ClienteEmpresa.objects.all()

    def get_object(self):
        id_cliente = self.kwargs.get("id")
        return get_object_or_404(self.queryset, id=id_cliente)


class ClientsCreate(views.CreateView):
    form_class = ClientsForm
    model = ClienteEmpresa.objects.all()
    template_name = 'alta_data/clients-add_update.html'
    success_url = reverse_lazy('alta_data:clientes')

    def form_valid(self, form):
        upper_form = upper_fields(self.model, form.save(commit=False))
        upper_form.save()
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accion'] = "Agrega datos para un nuevo perfil."
        context['boton'] = "Agregar"
        return context

class ClientsUpdate(views.UpdateView):
    form_class = ClientsForm
    model = ClienteEmpresa
    template_name = 'alta_data/clients-add_update.html'
    success_url = reverse_lazy('alta_data:clientes')

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(self.model, id=id_)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accion'] = "Actualizar perfil."
        context['boton'] = "actualizar"
        return context


class ClientsDelete(views.DeleteView):
    model = ClienteEmpresa
    template_name = 'alta_data/clients_delete.html'
    success_url = reverse_lazy('alta_data:clientes')

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(self.model, id=id_)

# #------------------------------------------------------------------------------------------------------------------
# #------------------------------------------------------------------------------------------------------------------
# #------------------------------------------------------------------------------------------------------------------#---------------------------------------- FACTURACIÓN ------------------------------------------------------
# #------------------------------------- CRUD Perfiles Certificado ------------------------------------------------------
class CertificateList(views.ListView):
    model = Certificado
    template_name = 'alta_data/certificate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['certificado'] = Certificado.objects.all()
        return context


class CertificateDetail(views.DetailView):
    template_name = 'alta_data/certificate_detail.html'
    queryset = Certificado.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(self.queryset, id=id_)


class CertificateCreate(views.CreateView):
    form_class = CertificateForm
    model = Certificado.objects.all()
    template_name = 'alta_data/certificate-add_update.html'
    success_url = reverse_lazy('alta_data:certificate')

    def form_valid(self, form):
        upper_form = upper_fields(self.model, form.save(commit=False))
        upper_form.save()
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accion'] = "Agrega datos para un nuevo perfil."
        context['boton'] = "agregar"
        return context


class CertificateUpdate(views.UpdateView):
    form_class = CertificateForm
    model = Certificado
    template_name = 'alta_data/certificate-add_update.html'
    success_url = reverse_lazy('alta_data:certificate')

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(self.model, id=id_)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accion'] = "Actualizar perfil."
        context['boton'] = "actualizar"
        return context


class CertificateDelete(views.DeleteView):
    model = Certificado
    template_name = 'alta_data/certificate_delete.html'
    success_url = reverse_lazy('alta_data:certificate')


    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(self.model, id=id_)   
# #------------------------------------------------------------------------------------------------------------------
# #------------------------------------------------------------------------------------------------------------------
# #------------------------------------------------------------------------------------------------------------------#---------------------------------------- FACTURACIÓN ------------------------------------------------------
# #------------------------------------- CRUD Perfiles Facturación ------------------------------------------------------
class BillingList(views.ListView):
    model = Facturacion
    template_name = 'alta_data/billing.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['facturacion'] = Facturacion.objects.all()
        return context


class BillingDetail(views.DetailView):
    template_name = 'alta_data/billing_detail.html'
    queryset = Facturacion.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(self.queryset, id=id_)


class BillingCreate(views.CreateView):
    form_class = BillingForm
    model = Facturacion.objects.all()
    template_name = 'alta_data/billing-add_update.html'
    success_url = reverse_lazy('alta_data:billing')

    def form_valid(self, form):
        upper_form = upper_fields(self.model, form.save(commit=False))
        upper_form.save()
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accion'] = "Agrega datos para un nuevo perfil."
        context['boton'] = "agregar"
        return context


class BillingUpdate(views.UpdateView):
    form_class = BillingForm
    model = Facturacion
    template_name = 'alta_data/billing-add_update.html'
    success_url = reverse_lazy('alta_data:billing')

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(self.model, id=id_)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['boton'] = "actualizar"
        context['accion'] = "Actualizar perfil."

        return context


class BillingDelete(views.DeleteView):
    model = Facturacion
    template_name = 'alta_data/billing_delete.html'
    success_url = reverse_lazy('alta_data:billing')

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(self.model, id=id_)
# #------------------------------------------------------------------------------------------------------------------
# #------------------------------------------------------------------------------------------------------------------
# #------------------------------------------------------------------------------------------------------------------#---------------------------------------- FACTURACIÓN ------------------------------------------------------
# #------------------------------------- CRUD Perfiles Contacto ------------------------------------------------------
class ContactProfileList(views.ListView):
    model = Contacto
    template_name = 'alta_data/contact_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacto'] = Contacto.objects.all()
        return context

class ContactProfileDetail(views.DetailView):
    template_name = 'alta_data/contact_profile_detail.html'
    queryset = Contacto.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(self.queryset, id=id_)


class ContactProfileCreate(views.CreateView):
    form_class = ContactProfieForm
    model = Contacto.objects.all()
    template_name = 'alta_data/contact_profile-add_update.html'
    success_url = reverse_lazy('alta_data:profile_contact')

    def form_valid(self, form):
        upper_form = upper_fields(self.model, form.save(commit=False))
        upper_form.save()
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accion'] = "Agrega datos para un nuevo perfil."
        context['boton'] = "agregar"
        return context


class ContactProfileUpdate(views.UpdateView):
    form_class = ContactProfieForm
    model = Contacto
    template_name = 'alta_data/contact_profile-add_update.html'
    success_url = reverse_lazy('alta_data:profile_contact')

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(self.model, id=id_)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accion'] = "Actualizar perfil."
        context['boton'] = "actualizar"
        return context


class ContactProfileDelete(views.DeleteView):
    model = Contacto
    template_name = 'alta_data/contact_profile_delete.html'
    success_url = reverse_lazy('alta_data:profile_contact')

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(self.model, id=id_)
# #------------------------------------------------------------------------------------------------------------------
# #------------------------------------------------------------------------------------------------------------------
# #------------------------------------------------------------------------------------------------------------------#---------------------------------------- FACTURACIÓN ------------------------------------------------------
# #------------------------------------- CRUD Perfiles de sitio ------------------------------------------------------
class SiteProfileList(views.ListView):
    model = Sitio
    template_name = 'alta_data/site_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sitio'] = Sitio.objects.all()
        return context


class SiteProfileDetail(views.DetailView):
    template_name = 'alta_data/site_profile_detail.html'
    queryset = Sitio.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(self.queryset, id=id_)


   
class SiteProfileCreate(views.CreateView):
    form_class = SiteCollectForm
    model = Sitio.objects.all()
    template_name = 'alta_data/site_profile-add_update.html'
    success_url = reverse_lazy('alta_data:profile_site')

    def form_valid(self, form):
        upper_form = upper_fields(self.model, form.save(commit=False))
        upper_form.save()
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accion'] = "Agrega datos para un nuevo perfil."
        context['boton'] = "agregar"
        return context


class SiteProfileUpdate(views.UpdateView):
    form_class = SiteCollectForm
    model = Sitio
    template_name = 'alta_data/site_profile-add_update.html'
    success_url = reverse_lazy('alta_data:profile_site')

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(self.model, id=id_)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accion'] = "Actualizar perfil."
        context['boton'] = "actualizar"
        return context


class SiteProfileDelete(views.DeleteView):
    model = Sitio
    template_name = 'alta_data/site_profile_delete.html'
    success_url = reverse_lazy('alta_data:profile_site')

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(self.model, id=id_)
# #------------------------------------------------------------------------------------------------------------------
# #------------------------------------------------------------------------------------------------------------------
# #------------------------------------------------------------------------------------------------------------------#---------------------------------------- FACTURACIÓN ------------------------------------------------------
# #------------------------------------- CRUD Instrumentos ------------------------------------------------------
class InstrumentsList(views.ListView):
    queryset = Instrumento.objects.all()
    template_name = 'alta_data/instruments.html'


class InstrumentsDetail(views.DetailView):
    template_name = 'alta_data/instruments_detail.html'
    queryset = Instrumento.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(self.queryset, id=id_)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = self.queryset
        return context


class InstrumentsCreate(views.CreateView):
    form_class = InstrumentsForm
    model = Instrumento.objects.all()
    template_name = 'alta_data/instruments-add_update.html'
    success_url = reverse_lazy('alta_data:instruments')

    def form_valid(self, form):
        upper_form = upper_fields(self.model, form.save(commit=False))
        upper_form.save()
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accion'] = "Agrega datos para un nuevo perfil."
        context['boton'] = "agregar"
        return context


class InstrumentsUpdate(views.UpdateView):
    form_class = InstrumentsForm
    model = Instrumento
    template_name = 'alta_data/instruments-add_update.html'
    success_url = reverse_lazy('alta_data:instruments')

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(self.model, id=id_)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accion'] = "Actualizar perfil."
        context['boton'] = "actualizar"
        return context


class InstrumentsDelete(views.DeleteView):
    model = Instrumento
    template_name = 'alta_data/instruments_delete.html'
    success_url = reverse_lazy('alta_data:instruments')

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(self.model, id=id_)
# #------------------------------------------------------------------------------------------------------------------
# #------------------------------------------------------------------------------------------------------------------
# #------------------------------------------------------------------------------------------------------------------
# #---------------------------------------- FACTURACIÓN ------------------------------------------------------
# #------------------------------------- CRUD Instrumentos en Sitio ------------------------------------------------------

# class InstrumentsSiteList(views.ListView):
#     queryset = Instrumentossitio.objects.all()
#     template_name = 'alta_data/instruments-site.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['model'] = self.queryset
#         return context

#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------- Orden de Servicio ----------------------------------------------------------
#--------------------------------------------------------- Lista ---------------------------------------------------------------
class ServiceOrderList(views.ListView):
    model = models_app.OrdenServicio
    template_name = 'ordenes_servicio/service_order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orden'] = models_app.OrdenServicio.objects.all()
        return context
#-------------------------------------------------------- Creación ---------------------------------------------------------------
#---------------------------------------------------- Test 2 ---------------------------------------------------------------------
# class ServiceOrderCreateView(SessionWizardView):
#     template_name = "../templates/ordenes_servicio/service_order_create.html"
#     form_list = [form_app.OrdenServicioFormulario1,
#                 form_app.OrdenServicioFormulario2,
#                 form_app.OrdenServicioFormulario3,
#                 form_app.OrdenServicioFormulario4,
#                 form_app.OrdenServicioFormulario5,
#                 form_app.OrdenServicioFormulario6,]

    # def post(self, request, *args, **kwargs):
    #     if request.POST.get('accion'):
    #         print("Esto es una llamada de AJAX")
    #         return HttpResponse(json.dumps({'hola': 'HOla mundo'}))
    #     else:
    #         return super().post(request)

#     def get(self, request, *args, **kwargs):
#         return super().get(request)

#     def get_context_data(self, form, **kwargs):
#         context= super().get_context_data(form, **kwargs)
#         context['optionCU'] = "0"

#         if self.request.method == 'POST':
#             context = self.get_query_objects(context)

#         return context

#     def get_query_objects(self, context, **kwargs):
#         prev_step = self.request.POST.get('service_order_create_view-current_step')

#         if prev_step == "0":
#             # cache.set("variable_x", self.request.user, 3600)
#             sitios_id = []
#             cliente = self.request.POST.get('0-id_cliente')
#             sitios_cliente = models_app.Sitio.objects.filter(id_empresa= cliente)

#             for sitio in sitios_cliente:
#                 sitios_id.append(sitio.id)

#             context['sitios_lista'] = sitios_id
#             context['servicio_sitio'] = form_app.ServicioSitioFormulario
#             context['recoleccion_entrega'] = form_app.RecoleccionEntregaFormulario
#             context['terceria'] = form_app.TerceriaFormulario

#         elif prev_step == "1":
#             pass
            # print("Preparados para guardar en cache")
            # cache.set("formularioPaso2", self.request.POST.get('razonsocial'), )
            
    #     return context

    # def done(self, form_list, **kwargs):
        # print(kwargs)
        # print("formularioPaso2: ", cache.get('formularioPaso2'))
        
        # len_forms = range(len(form_list))

        # for step in list(len_forms):
        #     if step == 0:
        #         sub_servicios = []

        #         if form_list[step].is_valid():
        #             formset_list = form_list[step]
        #             for form in formset_list:
        #                 print(form)
        #                 obj = form.save()
        #                 sub_servicios.append(obj.id)

        #     elif step == 1:
        #         if form_list[step].is_valid():
        #             form = form_list[step]
        #             servicio = form.save()
        #             servicio.estatus = models_app.Estatus.objects.get(id= 1)

        #             num_instrumentos = str(len(sub_servicios))
        #             servicio.no_certificado = "No Asignado"
        #             id = str(servicio.id).zfill(4)
        #             servicio.id_orden = "OS" + '-' + num_instrumentos + '-' + id

        #             for sub in sub_servicios:
        #                 servicio.id_subservicio.add(sub)

        #             servicio.save()

        # return redirect(servicio)
#---------------------------------------------------- Test 2 ---------------------------------------------------------------------
class ServiceOrderCreateView(views.FormView):
    template_name = "../templates/ordenes_servicio/service_order_create.html"
    form_class = form_app.OSFormulario1
    form_list = [form_class, form_app.OSFormulario2]
    paso = None

    def post(self, request, *args, **kwargs):
        flow_control = self.step_checker(request)
        

    def get(self, request, *args, **kwargs):
        flow_control = self.step_checker(request)
        self.paso = flow_control.get('paso')
        if self.paso == 1:
            context = self.get_context_data(form= self.form_list)

        return render(request, self.template_name, context= context)

    def get_context_data(self, form, **kwargs):
        context = super().get_context_data(**kwargs)
        print("Esto es la variable form: ", form)

        if self.paso == 1:
            context['form_list'] = self.forms_dict()
            context['paso'] = self.paso

        # print("Contexto: ", context)
        return context

    def step_checker(self, request):
        ajax = False
        if 'GET' in request.method:
            if request.GET.get('AJAXCall'):
                paso = request.POST.get('paso')
                ajax = True
            else:
                paso = 1
            submit = False
        else:
            if request.POST.get('paso'):
                paso = request.GET.get('paso')
            submit = True
        
        return {'paso': paso, 'submit': submit, 'ajax': ajax}

    def forms_dict(self):
        dict_keys = ['OrdenServicioForm', 'SubServicioForm']
        dict_form = {}
        i = self.paso - 1

        if self.paso == 1:
            key = dict_keys[i]
            form = self.form_list[i]
            dict_form[key] = form(filter= "RFC", **self.get_form_kwargs())

        return dict_form
#----------------------------------------------------- Actualización -------------------------------------------------------------
class ServiceOrderUpdateView(SessionWizardView):
    template_name = "../templates/ordenes_servicio/service_order_create.html"
    form_list = [form_app.OrdenServicioFormulario1,
                form_app.OrdenServicioFormulario2,
                form_app.OrdenServicioFormulario3,
                form_app.OrdenServicioFormulario4,
                form_app.OrdenServicioFormulario5,
                form_app.OrdenServicioFormulario6,]

    service_ID = "NoAsignado"
    services_num = "NoAsignado"

    def get_context_data(self, form, **kwargs):
        context= super().get_context_data(form, **kwargs)
        context['optionCU'] = "1"
        context['servicesNum'] = self.services_num
        
        return context

    def get_form_initial(self, step):
        self.service_ID = self.kwargs.get('id')
        service = models_app.OrdenServicio.objects.get(id= self.service_ID)
        
        if step == "0":
            sub_service = service.id_subservicio.all()
            self.services_num = len(sub_service)
            initial = self.initial_values(sub_service= sub_service)

        elif step == "1":
            initial = self.initial_values(service= service)

        return initial

    def done(self, form_list, **kwargs):
        len_forms = range(len(form_list))
        model_service = models_app.OrdenServicio.objects.get(id= self.kwargs.get('id'))
        model_subservice = model_service.id_subservicio.all()

        for step in list(len_forms):
            if step == 0:
                sub_servicios_set = []
                sub_servicios_add = []

                if form_list[step].is_valid():
                    formset_list = form_list[step]

                    for form in formset_list:
                        if form.cleaned_data['hidden_field'] != "":
                            id_sub_service = form.cleaned_data['hidden_field']
                            sub_ser = model_subservice.get(id= int(id_sub_service))
                            print("form cleaned: ", form.cleaned_data['id_instrumento'])

                            sub_ser.id_instrumento.set([instr for instr in form.cleaned_data['id_instrumento']])
                            sub_ser.id_sitio = form.cleaned_data['id_sitio']
                            sub_ser.id_certificado = form.cleaned_data['id_certificado']

                            sub_ser.save()
                            sub_servicios_set.append(sub_ser.id)
                        else:
                            obj = form.save()
                            sub_servicios_add.append(obj.id)

            elif step == 1:
                if form_list[step].is_valid():
                    form = form_list[step]

                    model_service.id_facturacion = form.cleaned_data['id_facturacion']
                    model_service.dia_servicio = form.cleaned_data['dia_servicio']
                    model_service.observaciones = form.cleaned_data['observaciones']

                    model_service.id_subservicio.set([sub for sub in sub_servicios_set])

                    if len(sub_servicios_add) != 0:
                        for sub in sub_servicios_add:
                            model_service.id_subservicio.add(sub)

                    model_service.save()

        return redirect(model_service)

    def initial_values(self, *args, **kwargs):
        if "sub_service" in kwargs.keys():
            initial_vals = []
            
            for item in kwargs.get('sub_service'):
                initial_dict = {}
                initial_dict['hidden_field'] = item.id
                initial_dict["id_sitio"] = [item.id_sitio.id]
                initial_dict["id_certificado"] = [item.id_certificado.id]
                instruments = []

                for instrument in item.id_instrumento.all():
                    instruments.append(instrument.id)

                initial_dict["id_instrumento"] = instruments
                initial_vals.append(initial_dict)
        
        elif "service" in kwargs.keys():
            service = kwargs.get('service')
            initial_vals = {}

            initial_vals['id_facturacion'] = [service.id_facturacion.id]
            initial_vals['observaciones'] = service.observaciones
            
            date = service.dia_servicio
            initial_vals['dia_servicio'] = str(date)[:-9].replace(" ", "T")
        
        return initial_vals

#-------------------------------------------------------- Detalles ---------------------------------------------------------------
class ServiceOrderDetailView(views.DetailView):
    template_name = "../templates/ordenes_servicio/service_order_detail.html"
    model = models_app.OrdenServicio

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date = context['object'].dia_servicio
        date = str(date)[:-9].replace(" ", "T")
        context['new_format'] = date
        return context

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(self.model, id= id_)
#-------------------------------------------------------- Eliminar ---------------------------------------------------------------

#--------------------------------------------------------- PDF -----------------------------------------------------------------
def export_pdf(request, **kwargs):
    id_n = kwargs.get('id')
    #facturacion = BillingData.objects.filter(rfc_data__in=['DML7905239C4'])
    orden_servicio = models_app.OrdenServicio.objects.get(id=id_n)

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
