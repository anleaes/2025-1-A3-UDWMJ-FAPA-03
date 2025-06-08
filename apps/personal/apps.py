from django.apps import AppConfig


class PersonalConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.personal"  # <--- CORRETO para apps dentro de "apps/"
    verbose_name = "Personal"
