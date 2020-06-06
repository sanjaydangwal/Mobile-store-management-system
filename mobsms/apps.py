from django.apps import AppConfig


class MobsmsConfig(AppConfig):
    name = 'mobsms'

    def ready(self):
        from mobsms import signals
