from django.contrib import admin

# Register your models here.
from .models import Pet, Usuario, Ong, Endereco, Vacina

class PetsAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'idade', 'raca', 'sexo', 'tipo', 'porte', 'pelo', 'descricao','foto', 'usuario', 'ong')
    list_display_links = ('id','nome', 'idade', 'raca', 'sexo', 'tipo', 'porte', 'pelo', 'descricao','foto', 'usuario', 'ong')
    search_fields = ('id','nome', 'idade', 'raca', 'sexo', 'tipo', 'porte', 'pelo', 'descricao','foto', 'usuario', 'ong')
    list_per_page = 10

class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'email', 'senha', 'telefone')
    list_display_links = ('id','nome', 'email', 'senha', 'telefone')
    search_fields = ('id','nome', 'email', 'senha', 'telefone')
    list_per_page = 10

class OngsAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'email', 'senha', 'telefone', 'cnpj')
    list_display_links = ('id','nome', 'email', 'senha', 'telefone', 'cnpj')
    search_fields = ('id','nome', 'email', 'senha', 'telefone', 'cnpj')
    list_per_page = 10

class EnderecosAdmin(admin.ModelAdmin):
    list_display = ('rua', 'numero', 'bairro', 'cidade', 'estado', 'cep')
    list_display_links = ('rua', 'numero', 'bairro', 'cidade', 'estado', 'cep')
    search_fields = ('rua', 'numero', 'bairro', 'cidade', 'estado', 'cep')
    list_per_page = 10

class VacinasAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'data', 'pet')
    list_display_links = ('id','nome', 'data', 'pet')
    search_fields = ('id','nome', 'data', 'pet')
    list_per_page = 10

admin.site.register(Pet, PetsAdmin)
admin.site.register(Usuario, UsuariosAdmin)
admin.site.register(Ong, OngsAdmin)
admin.site.register(Endereco, EnderecosAdmin)
admin.site.register(Vacina, VacinasAdmin)