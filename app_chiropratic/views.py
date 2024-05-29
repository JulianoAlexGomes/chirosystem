from django.shortcuts import render, redirect, get_object_or_404
from .models import cadastro_patologias
from django.core.paginator import Paginator

def cadastro_patologia(request):
    return render(request, 'cadastros/patologias/cadastro_patologias.html')

def patologia(request):
    if request.method == 'POST':
        nova_patologia = cadastro_patologias(
            patologia=request.POST.get('patologia'),
            sintomas=request.POST.get('sintomas'),
            observacoes=request.POST.get('obs')
        )
        nova_patologia.save()
        message = "Patologia cadastrada com sucesso!"
        return render(request, 'cadastros/patologias/cadastro_patologias.html', {'message': message})

    patologias_cadastradas = {
        'patologias': cadastro_patologias.objects.all()
    }
    return render(request, 'cadastros/patologias/patologias.html', patologias_cadastradas)

def lista_patologias(request):
    patologias_list = cadastro_patologias.objects.all()
    paginator = Paginator(patologias_list, 40)  # Mostra 40 patologias por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'cadastros/patologias/patologias.html', {'page_obj': page_obj})

def pagina_home(request):
    return render(request, 'cadastros/patologias/home.html')

def delete_patologia(request, id):
    patologia = get_object_or_404(cadastro_patologias, id=id)
    patologia.delete()
    return redirect('lista_patologias')

def edit_patologia(request, id):
    patologia = get_object_or_404(cadastro_patologias, id=id)
    if request.method == 'POST':
        patologia.patologia = request.POST.get('patologia')
        patologia.sintomas = request.POST.get('sintomas')
        patologia.observacoes = request.POST.get('obs')
        patologia.save()
        return redirect('lista_patologias')
    return render(request, 'cadastros/patologias/edit_patologia.html', {'patologia': patologia})
