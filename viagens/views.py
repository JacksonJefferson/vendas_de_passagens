from django.shortcuts import render, redirect
from . models import Passagem, Veiculo
from . forms import PassagemForm, VeiculoForm

def home(request):
    return render (request, 'home.html')

def passagem_list(request):
    passagens = Passagem.objects.all()
    return render (request, 'passagem/list.html', {'passagens': passagens})

def passagem_show(request, passagem_id):
    passagem = Passagem.objects.get(id=passagem_id)
    return render (request, 'passagem/show.html', {'passagem': passagem})

def passagem_form(request):
    if (request.method == "POST"):
        form = PassagemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/viagens/passagem/')
        else:
            return render (request, 'passagem/form.html', {'form': form})
    else:
        form = VeiculoForm()
        return render (request, 'passagem/form.html', {'form': form})


def veiculo_form(request):
    if (request.method == "POST"):
        form = VeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/viagens/veiculo/')
        else:
            return render (request, 'veiculo/form.html', {'form': form})
    else:
        form = VeiculoForm()
        return render (request, 'veiculo/form.html', {'form': form})


def veiculo_list(request):
    veiculos = Veiculo.objects.all()
    return render (request, 'veiculo/list.html', {'veiculos': veiculos})

def veiculo_show(request, veiculo_id):
    veiculo = Veiculo.objects.get(id=veiculo_id)
    return render (request, 'veiculo/show.html', {'veiculo': veiculo})

