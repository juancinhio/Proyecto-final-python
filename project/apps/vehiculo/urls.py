from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "vehiculo"

urlpatterns = [
    path("", TemplateView.as_view(template_name="vehiculo/index.html"), name="home"),
    path("create/<int:cliente_id>/", views.VehiculoCreate.as_view(), name="create"),
    path("detail/", views.VehiculoDetail.as_view(), name="detail"),
    path("list/", views.VehiculoList.as_view(), name="list"),
    path("update/<int:vehiculo_id>", views.VehiculoUpdate.as_view(), name="update"),
    
]