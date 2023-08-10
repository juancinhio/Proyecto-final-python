from django.urls import path
from django.views.generic import TemplateView

from . import views
app_name = "cliente"


urlpatterns = [

    path("", TemplateView.as_view(template_name="cliente/index.html"), name="home"),
    path("create/", views.ClienteCreate.as_view(), name="create"),
    path("detail/", views.ClienteDetail.as_view(), name="detail"),
    path("list/", views.ClienteList.as_view(), name="list"),
    path("update/<int:cliente_id>",views.ClienteUpdate.as_view(),name="update"),
    

]    