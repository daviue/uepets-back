from django.contrib import admin

# Register your models here.
from .models import Pet, Usuario, Ong, Endereco, Vacina

admin.site.register(Pet)
admin.site.register(Usuario)
admin.site.register(Ong)
admin.site.register(Endereco)
admin.site.register(Vacina)