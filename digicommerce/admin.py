from digicommerce.models import Categoria, Marca, Produto
from django.contrib import admin
from .models import *

admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Endereco)

