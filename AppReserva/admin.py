from django.contrib import admin


from .models import Reserva, Timer, Sectores
# Register your models here.

admin.site.register(Reserva)
admin.site.register(Timer)
admin.site.register(Sectores)