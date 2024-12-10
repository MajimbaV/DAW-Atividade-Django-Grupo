# Atividade Avaliativa Individual do 3º Bimestre
Esse repositório foi criado como uma atividade avaliativa em grupo para o 3º Bimestre da disciplina de Desenvolvolvimento de Aplicações Web, especificamente sobre o conteúdo
de Django, ministrado em sala.

A app criada como exemplo tem como escôpo um sistema de lojas genérico, o que inclui as seguintes entidades:

- Cliente
- Categoria de Produtos
- Produtos
- Pedidos
- Funcionários
- Departamentos

As entidades foram descritas como classes e implementadas como models do app "loja".

Antes de iniciar a aplicação, é recomendada a criação de um ambiente virtual python, devido a suas dependências, para isso, utilize do seguinte comando no terminal:
```
python3 -m venv venv
```
Para o funcionamento do projeto é necessário, primordialmente, instalar as dependências com o comando
```
pip install Django
```
Em seguida, deve-se rodar o servidor com o projeto através do seguinte comando e, então, abrir o endereço local
```
python3 manage.py runserver
```
Caso se tenha interesse em adcionar instâncias o usuário deve realizar o cadastro de um super usuário atráves do seguinte comando no terminal:
```
python3 manage.py createsuperuser
```
E então fornecer as informações. O superusuário deve logar através da página de login do sistema
