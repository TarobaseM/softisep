from django.shortcuts import render
from .models import Cours, Logiciel
from .forms import SearchForm
from django.shortcuts import render, get_object_or_404

def index(request):
    form = SearchForm(request.GET or None)
    cours_list = Cours.objects.all()

    if form.is_valid():
        query = form.cleaned_data['query']
        cours_list = cours_list.filter(nom__icontains=query)

    context = {
        'form': form,
        'cours_list': cours_list,
    }
    return render(request, 'index.html', context)

def logiciel_view(request, logiciel_name):
    logiciel = get_object_or_404(Logiciel, nom=logiciel_name)
    cours_associated = logiciel.cours_logiciels.all()
    context = {
        'logiciel': logiciel,
        'cours_associated': cours_associated,
    }
    return render(request, 'page_logiciel.html', context)