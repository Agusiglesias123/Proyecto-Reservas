from django.contrib import admin


from .models import Reserva, Timer
# Register your models here.

admin.site.register(Reserva)
admin.site.register(Timer)