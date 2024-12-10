from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, CategoriaProduto, Produto, Pedido, Funcionario, Departamento
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound
from django.contrib.auth import login, logout
import datetime

# Create your views here.

# Core

def home(request):
    return render(request, 'home.html')

def cria_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.create_user(username, email, password)
        user.save()
        login(request, user)
        return redirect('home')
    return render(request, 'registration/registro.html')

def user_logout(request):
    logout(request)
    return redirect('home')

#Cliente

def lista_cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/lista-cliente.html', {"clientes": clientes})

def cria_cliente(request):
    if not request.user.is_staff:
        return HttpResponseNotFound("")
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        telefone = request.POST.get("telefone")
        endereco = request.POST.get("endereco")
        cliente = Cliente()
        cliente.nome = nome
        cliente.email = email
        cliente.telefone = telefone
        cliente.endereco = endereco
        cliente.save()
        return redirect('lista-cliente')
    return render(request, 'cliente/form-cliente.html')

def atualiza_cliente(request, id):
    if not request.user.is_staff:
        return HttpResponseNotFound("")
    cliente = get_object_or_404(Cliente, pk=id)
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        telefone = request.POST.get("telefone")
        endereco = request.POST.get("endereco")
        cliente.nome = nome
        cliente.email = email
        cliente.telefone = telefone
        cliente.endereco = endereco
        cliente.save()
        return redirect('lista-cliente')
    return render(request, 'cliente/form-cliente.html', {"cliente": cliente})

def remove_cliente(request, id):
    if not request.user.is_staff:
        return HttpResponseNotFound("")
    cliente = get_object_or_404(Cliente, pk=id)
    cliente.delete()
    return redirect('lista-cliente')

# Categoria de Produtos

def lista_categoria(request):
    categorias = CategoriaProduto.objects.all()
    return render(request, 'categoria/lista-categoria.html', {"categorias": categorias})

def cria_categoria(request):
    if not request.user.is_staff:
        return HttpResponseNotFound("")
    if request.method == "POST":
        nome = request.POST.get("nome")
        descricao = request.POST.get("descricao")
        categoria = CategoriaProduto()
        categoria.nome = nome
        categoria.descricao = descricao
        categoria.save()
        return redirect('lista-categoria')
    return render(request, 'categoria/form-categoria.html')

def atualiza_categoria(request, id):
    if not request.user.is_staff:
        return HttpResponseNotFound("")
    categoria = get_object_or_404(CategoriaProduto, pk=id)
    if request.method == "POST":
        nome = request.POST.get("nome")
        descricao = request.POST.get("descricao")
        categoria.nome = nome
        categoria.descricao = descricao
        categoria.save()
        return redirect('lista-categoria')
    return render(request, 'categoria/form-categoria.html', {"categoria": categoria})

def remove_categoria(request, id):
    if not request.user.is_staff:
        return HttpResponseNotFound("")
    categoria = get_object_or_404(CategoriaProduto, pk=id)
    categoria.delete()
    return redirect('lista-categoria')


#Produtos

def lista_produto(request):
    produtos = Produto.objects.all()
    return render(request, 'produto/lista-produto.html', {"produtos": produtos})

def cria_produto(request):
    if not request.user.is_staff:
        return HttpResponseNotFound("")
    categorias = CategoriaProduto.objects.all()
    if request.method == "POST":
        nome = request.POST.get("nome")
        descricao = request.POST.get("descricao")
        preco = request.POST.get("preco")
        estoque = request.POST.get("estoque")
        categoriaID = request.POST.get("categoria")
        produto = Produto()
        produto.nome = nome
        produto.descricao = descricao
        produto.preco = preco
        produto.estoque = estoque
        produto.categoria = get_object_or_404(CategoriaProduto, pk=categoriaID)
        produto.save()
        return redirect('lista-produto')
    return render(request, 'produto/form-produto.html', {"categorias": categorias})

def atualiza_produto(request, id):
    if not request.user.is_staff:
        return HttpResponseNotFound("")
    produto = get_object_or_404(Produto, pk=id)
    categorias = CategoriaProduto.objects.all()
    if request.method == "POST":
        nome = request.POST.get("nome")
        descricao = request.POST.get("descricao")
        preco = request.POST.get("preco")
        estoque = request.POST.get("estoque")
        categoriaID = request.POST.get("categoria")
        produto.nome = nome
        produto.descricao = descricao
        produto.preco = preco
        produto.estoque = estoque
        produto.categoria = get_object_or_404(CategoriaProduto, pk=categoriaID)
        produto.save()
        return redirect('lista-produto')
    return render(request, 'produto/form-produto.html', {"produto": produto, "categorias": categorias})

def remove_produto(request, id):
    if not request.user.is_staff:
        return HttpResponseNotFound("")
    produto = get_object_or_404(Produto, pk=id)
    produto.delete()
    return redirect('lista-produto')

# Pedidos

def lista_pedido(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedido/lista-pedido.html', {"pedidos": pedidos})

def cria_pedido(request):
    if not request.user.is_staff:
        return HttpResponseNotFound("")
    clientes = Cliente.objects.all()
    produtos = Produto.objects.all()
    if request.method == "POST":
        clienteID = request.POST.get("cliente")
        data = request.POST.get("data")
        produtos = request.POST.getlist("produtos")
        pedido = Pedido()
        pedido.cliente = get_object_or_404(Cliente, pk=clienteID)
        pedido.dataPedido =  datetime.datetime.strptime(data, '%Y-%m-%d').date()
        pedido.save()
        for produto in produtos:
            pedido.produtos.add(produto)
        return redirect('lista-pedido')
    return render(request, 'pedido/form-pedido.html', {"clientes": clientes, "produtos": produtos, "data_atual": datetime.datetime.now().strftime("%Y-%m-%d")})

def atualiza_pedido(request, id):
    if not request.user.is_staff:
        return HttpResponseNotFound("")
    pedido = get_object_or_404(Pedido, pk=id)
    clientes = Cliente.objects.all()
    produtos = Produto.objects.all()
    if request.method == "POST":
        clienteID = request.POST.get("cliente")
        data = request.POST.get("data")
        produtos = request.POST.getlist("produtos")
        pedido.cliente = get_object_or_404(Cliente, pk=clienteID)
        pedido.dataPedido =  datetime.datetime.strptime(data, '%Y-%m-%d').date()
        pedido.save()
        for produto_registrado in pedido.produtos.all():
            if produto_registrado not in produtos:
                pedido.produtos.remove(produto_registrado)
        for produto in produtos:
            pedido.produtos.add(produto)
        return redirect('lista-pedido')
    return render(request, 'pedido/form-pedido.html', {"pedido": pedido, "clientes": clientes, "produtos": produtos})

def remove_pedido(request, id):
    if not request.user.is_staff:
        return HttpResponseNotFound("")
    pedido = get_object_or_404(Pedido, pk=id)
    pedido.delete()
    return redirect('lista-pedido')


# Funcionário

def lista_funcionario(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'funcionario/lista-funcionario.html', {"funcionarios": funcionarios})

def cria_funcionario(request):
    if not request.user.is_staff:
        return HttpResponseNotFound("")
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        cargo = request.POST.get("cargo")
        telefone = request.POST.get("telefone")
        endereco = request.POST.get("endereco")
        funcionario = Funcionario()
        funcionario.nome = nome
        funcionario.email = email
        funcionario.cargo = cargo
        funcionario.telefone = telefone
        funcionario.endereco = endereco
        funcionario.save()
        return redirect('lista-funcionario')
    return render(request, 'funcionario/form-funcionario.html')

def atualiza_funcionario(request, id):
    if not request.user.is_staff:
        return HttpResponseNotFound("")
    funcionario = get_object_or_404(Funcionario, pk=id)
    if request.method == "POST":
        nome = request.POST.get("nome")
        cargo = request.POST.get("cargo")
        email = request.POST.get("email")
        telefone = request.POST.get("telefone")
        endereco = request.POST.get("endereco")
        funcionario.nome = nome
        funcionario.cargo = cargo
        funcionario.email = email
        funcionario.telefone = telefone
        funcionario.endereco = endereco
        funcionario.save()
        return redirect('lista-funcionario')
    return render(request, 'funcionario/form-funcionario.html', {"funcionario": funcionario})

def remove_funcionario(request, id):
    if not request.user.is_staff:
        return HttpResponseNotFound("")
    funcionario = get_object_or_404(Funcionario, pk=id)
    funcionario.delete()
    return redirect('lista-funcionario')


# Departamento

def lista_departamento(request):
    departamentos = Departamento.objects.all()
    return render(request, 'departamento/lista-departamento.html', {"departamentos": departamentos})

def cria_departamento(request):
    if not request.user.is_staff:
        return HttpResponseNotFound("")
    funcionarios = Funcionario.objects.all()
    if request.method == "POST":
        nome = request.POST.get("nome")
        endereco = request.POST.get("endereco")
        funcionarios = request.POST.getlist("funcionarios")
        departamento = Departamento()
        departamento.nome = nome
        departamento.endereco = endereco
        departamento.save()
        for funcionario in funcionarios:
            departamento.funcionarios.add(funcionario)
        return redirect('lista-departamento')
    return render(request, 'departamento/form-departamento.html', {"funcionarios": funcionarios})

def atualiza_departamento(request, id):
    if not request.user.is_staff:
        return HttpResponseNotFound("")
    departamento = get_object_or_404(Departamento, pk=id)
    funcionarios = Funcionario.objects.all()
    if request.method == "POST":
        nome = request.POST.get("nome")
        endereco = request.POST.get("endereco")
        funcionarios = request.POST.getlist("funcionarios")
        departamento.nome = nome
        departamento.endereco =  endereco
        departamento.save()
        for funcionario_registrado in departamento.funcionarios.all():
            if funcionario_registrado.id not in funcionarios:
                departamento.funcionarios.remove(funcionario_registrado)
        for funcionario in funcionarios:
            departamento.funcionarios.add(funcionario)
        return redirect('lista-departamento')
    return render(request, 'departamento/form-departamento.html', {"departamento": departamento, "funcionarios": funcionarios})

def remove_departamento(request, id):
    if not request.user.is_staff:
        return HttpResponseNotFound("")
    departamento = get_object_or_404(Departamento, pk=id)
    departamento.delete()
    return redirect('lista-departamento')