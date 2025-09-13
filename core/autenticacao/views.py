from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.


def entrar(request):

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username = username, password=password)

		if user:
			auth.login(request, user)
			return redirect("/")
		else:
			messages.info(request, 'Email ou senha incorrectos. Verifique e tente novamente!')
			return redirect("entrar")

	else:
		return render(request, "entrar.html")

def cadastro(request):

	if request.method == 'POST':

		username = request.POST['username']
		email = request.POST["email"]
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		if password1==password2:
			if User.objects.filter(username=username).exists:
				messages.info(request, "Username usado!")
				return redirect('cadastro')

			elif User.objects.filter(email=email).exists:
				messages.info(request, 'Esse E-mail já foi usado!')
				return redirect('cadastro')

			else:
				user = User.objects.create_user(username=username, email=email, password=password1)
				user.save()
				messages.success(request, 'Usuário criado com sucesso!')
				return redirect('login')

		else:
			messages.info(request, 'As palavras-passe devem ser iguais!')
			return redirect('cadastro')
	else: 
		return render(request, 'cadastro.html')

def sair(request):
    auth.logout(request)
    return redirect('/')