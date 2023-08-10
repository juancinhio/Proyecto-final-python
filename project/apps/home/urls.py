from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import home
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from . import views

app_name = "home"

urlpatterns = [
    path("", views.home, name="home"),
    path('login/', views.login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="Home/logout.html"), name="logout"),
    path('about/', TemplateView.as_view(template_name="Home/about.html"), name="about"),
    path('register/', views.register, name="register"),


]

urlpatterns += staticfiles_urlpatterns()