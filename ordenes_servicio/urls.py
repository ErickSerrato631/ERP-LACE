from . import views
from django.urls import path

app_name = 'ordenes_servicio'

urlpatterns = [
    path('service_order/', views.ServiceOrderCreateView.as_view(), name= "OrdenServicio"),
    path('service_order_detail/<int:id>/', views.ServiceOrderDetailView.as_view(), name= "service_order_detail"),
    # path('service_order_update/<int:id>/', views.ServiceOrderUpdateView.as_view(), name= "service_order_update"),
    # path('service_order/', views.ServiceOrderCreateView.as_view(), name= "OrdenServicio"),
    # path('service_order_detail/<int:id>/', views.ServiceOrderDetailView.as_view(), name= "service_order_detail"),
    # path('service_order_update/<int:id>/', views.ServiceOrderUpdateView.as_view(), name= "service_order_update"),

    path('OS_PDF/<int:id>/', views.export_pdf, name="OS_PDF"),
    path('orden_servicio_list/', views.ServiceOrderList.as_view(), name='orden_servicio_list'),

]
