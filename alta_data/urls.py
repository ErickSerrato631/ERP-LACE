from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'alta_data'

urlpatterns = [
    #------------------------------------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------------------------------------#---------------------------------------- FACTURACIÓN ------------------------------------------------------
    #------------------------------------- CRUD Clientes ------------------------------------------------------
    path('clientes/', views.ClientsList.as_view(), name='clientes'),
    path('clients_detail/<int:id>/', views.ClientsDetail.as_view(), name = 'clients_detail'),
    path('clients-add/', views.ClientsCreate.as_view(),name='clients-add'),
    path('clients_update/<int:id>/', views.ClientsUpdate.as_view(), name='clients_update'),
    path('clients_delete/<int:id>/',views.ClientsDelete.as_view(), name='clients_delete'),

    #------------------------------------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------------------------------------#---------------------------------------- FACTURACIÓN ------------------------------------------------------
    #------------------------------------- CRUD Perfiles Certificado ------------------------------------------------------
    path('certificate/', views.CertificateList.as_view(), name='certificate'),
    path('certificate_detail/<int:id>/',views.CertificateDetail.as_view(), name='certificate_detail'),
    path('certificate-add/', views.CertificateCreate.as_view(),name='certificate-add'),
    path('certificate_update/<int:id>/', views.CertificateUpdate.as_view(), name='certificate_update'),
    path('certificate_delete/<int:id>/', views.CertificateDelete.as_view(), name='certificate_delete'),
    #------------------------------------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------------------------------------#---------------------------------------- FACTURACIÓN ------------------------------------------------------
    #------------------------------------- CRUD Perfiles Certificado ------------------------------------------------------
    path('billing/', views.BillingList.as_view(), name='billing'),
    path('billing_detail/<int:id>/',views.BillingDetail.as_view(), name='billing_detail'),
    path('billing-add/', views.BillingCreate.as_view(),name='billing-add'),
    path('billing_update/<int:id>/', views.BillingUpdate.as_view(), name='billing_update'),
    path('billing_delete/<int:id>/', views.BillingDelete.as_view(), name='billing_delete'),

    #------------------------------------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------------------------------------#---------------------------------------- FACTURACIÓN ------------------------------------------------------
    #------------------------------------- CRUD Perfiles Certificado ------------------------------------------------------
    path('profile_contact/', views.ContactProfileList.as_view(),name='profile_contact'),
    path('profile_contact_detail/<int:id>/',views.ContactProfileDetail.as_view(), name='profile_contact_detail'),
    path('profile_contact-add/', views.ContactProfileCreate.as_view(),name='profile_contact-add'),
    path('profile_contact_update/<int:id>/', views.ContactProfileUpdate.as_view(), name='profile_contact_update'),
    path('profile_contact_delete/<int:id>/', views.ContactProfileDelete.as_view(), name='profile_contact_delete'),

    #------------------------------------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------------------------------------#---------------------------------------- FACTURACIÓN ------------------------------------------------------
    #------------------------------------- CRUD Perfiles Sitio ------------------------------------------------------
    path('profile_site/', views.SiteProfileList.as_view(),name='profile_site'),
    path('profile_site_detail/<int:id>/',views.SiteProfileDetail.as_view(), name='profile_site_detail'),
    path('profile_site-add/', views.SiteProfileCreate.as_view(),name='profile_site-add'),
    path('profile_site_update/<int:id>/', views.SiteProfileUpdate.as_view(), name='profile_site_update'),
    path('profile_site_delete/<int:id>/', views.SiteProfileDelete.as_view(), name='profile_site_delete'),

    #------------------------------------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------------------------------------#---------------------------------------- FACTURACIÓN ------------------------------------------------------
    #------------------------------------- CRUD Instrumentos ------------------------------------------------------
    path('instruments/', views.InstrumentsList.as_view(),name='instruments'),
    path('instruments_detail/<int:id>/',views.InstrumentsDetail.as_view(), name='instruments_detail'),
    path('instruments-add/', views.InstrumentsCreate.as_view(),name='instruments-add'),   
    path('instruments_update/<int:id>/', views.InstrumentsUpdate.as_view(), name='instruments_update'),
    path('instruments_delete/<int:id>/', views.InstrumentsDelete.as_view(), name='instruments_delete'),

    #------------------------------------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------------------------------------#---------------------------------------- FACTURACIÓN ------------------------------------------------------
    #------------------------------------- CRUD Instrumentos en Sitio------------------------------------------------------
    # path('instruments-site/', views.InstrumentsSiteList.as_view(),
    #      name='instruments-site'),
    # path('instruments-site/', views.InstrumentsSiteList.as_view(),name='instruments-site'),
    # path('instruments-site-add/', views.InstrumentsSiteCreate.as_view(),name='instruments-site-add'),
    # path('instruments-site_update/<int:id>/', views.InstrumentsSiteUpdate.as_view(), name='instruments-site_update'),
    # path('instruments_site_delete/<int:id>/', views.InstrumentsDelete.as_view(), name='instruments_site_delete'),
]
