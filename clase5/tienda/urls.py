from django.urls import path

from . import views

urlpatterns = [
    path("<slug:clave>",views.vista_categoria,name="vista_categoria"),
    path("<slug:clave>/<slug:clave_prod>",views.vista_producto,name="vista_producto")
]