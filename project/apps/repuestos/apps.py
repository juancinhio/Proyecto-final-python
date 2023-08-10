from django.apps import AppConfig

class RepuestosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'repuestos'

    def ready(self):
        from . import data_loader 
        data_loader.load_data()  
