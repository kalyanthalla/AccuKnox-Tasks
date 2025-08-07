from django.apps import AppConfig

class SignalsDemoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'signals_demo'

    def ready(self):
        # Import and connect signals
        import signals_demo.signals