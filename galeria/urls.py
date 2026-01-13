from django.urls import path
from galeria.views import index # importação da view index para poder usá-la nas rotas
from galeria.views import contatos # importação da view contatos para poder usá-la nas rotas

urlpatterns = [
     path('', index), # rota raiz direciona para a view index.
     path('contatos', contatos) # nova rota para a view contatos
     # views é onde ficam as funções que processam as requisições, em views.py
]
