from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registro', views.cria_user, name='registro'),
    path('accounts/logout', views.user_logout, name='logout'),
    path('cliente', views.lista_cliente, name='lista-cliente'),
    path('cliente/criar', views.cria_cliente, name='cria-cliente'),
    path('cliente/atualizar/<int:id>', views.atualiza_cliente, name='atualiza-cliente'),
    path('cliente/remover/<int:id>', views.remove_cliente, name='remove-cliente'),
    path('categoria', views.lista_categoria, name='lista-categoria'),
    path('categoria/criar', views.cria_categoria, name='cria-categoria'),
    path('categoria/atualizar/<int:id>', views.atualiza_categoria, name='atualiza-categoria'),
    path('categoria/remover/<int:id>', views.remove_categoria, name='remove-categoria'),
    path('produto', views.lista_produto, name='lista-produto'),
    path('produto/criar', views.cria_produto, name='cria-produto'),
    path('produto/atualizar/<int:id>', views.atualiza_produto, name='atualiza-produto'),
    path('produto/remover/<int:id>', views.remove_produto, name='remove-produto'),
    path('pedido', views.lista_pedido, name='lista-pedido'),
    path('pedido/criar', views.cria_pedido, name='cria-pedido'),
    path('pedido/atualizar/<int:id>', views.atualiza_pedido, name='atualiza-pedido'),
    path('pedido/remover/<int:id>', views.remove_pedido, name='remove-pedido'),
    path('funcionario', views.lista_funcionario, name='lista-funcionario'),
    path('funcionario/criar', views.cria_funcionario, name='cria-funcionario'),
    path('funcionario/atualizar/<int:id>', views.atualiza_funcionario, name='atualiza-funcionario'),
    path('funcionario/remover/<int:id>', views.remove_funcionario, name='remove-funcionario'),
    path('departamento', views.lista_departamento, name='lista-departamento'),
    path('departamento/criar', views.cria_departamento, name='cria-departamento'),
    path('departamento/atualizar/<int:id>', views.atualiza_departamento, name='atualiza-departamento'),
    path('departamento/remover/<int:id>', views.remove_departamento, name='remove-departamento'),
]