from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = 'repuestos'

urlpatterns = [
    path("", TemplateView.as_view(template_name="repuestos/repuestos.html"), name="home"),
    path("afinacion/", views.AfinacionView.as_view(), name="afinacion"),
    path("frenos/", views.FrenosView.as_view(), name="frenos"),
    path("suspencion/", views.SuspensionView.as_view(), name="suspencion"),
    path("service/", views.ServiceView.as_view(), name="service"),
    path("embrague/", views.EmbragueView.as_view(), name="embrague"),
    path("distribucion/", views.DistribucionView.as_view(), name="distribucion"),
    path("circuito/", views.CircuitoView.as_view(), name="circuito"),
    path("electricidad/", views.ElectricidadView.as_view(), name="electricidad"),
    path("motor/", views.MotorView.as_view(), name="motor"),
    path("otros/", views.OtrosView.as_view(), name="otros"),
 
     
]

