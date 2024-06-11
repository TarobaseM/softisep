from django.shortcuts import render, get_object_or_404, redirect
from .models import Cours, Logiciel
from .forms import SearchForm

def index(request):
    """
    Vue principale qui affiche la liste des cours et gère la recherche par nom.
    """
    # Initialisation du formulaire de recherche avec les données GET
    form = SearchForm(request.GET or None)
    cours_list = Cours.objects.all()

    # Filtrage des cours si le formulaire est valide
    if form.is_valid():
        query = form.cleaned_data['query']
        cours_list = cours_list.filter(nom__icontains=query)

    context = {
        'form': form,
        'cours_list': cours_list,
    }
    return render(request, 'index.html', context)

def logiciel_view(request, logiciel_name):
    """
    Vue qui affiche les détails d'un logiciel spécifique et les cours associés.
    """
    logiciel = get_object_or_404(Logiciel, nom=logiciel_name)
    cours_associated = logiciel.cours_logiciels.all()
    
    context = {
        'logiciel': logiciel,
        'cours_associated': cours_associated,
    }
    return render(request, 'page_logiciel.html', context)

def my_courses(request):
    """
    Vue qui affiche les cours de l'utilisateur connecté.
    Redirige vers la page d'accueil si l'utilisateur n'est pas authentifié.
    """
    if request.user.is_authenticated:
        courses = request.user.cours.all()
    else:
        return redirect('index')
    
    context = {
        'courses': courses,
    }
    return render(request, 'my_courses.html', context)
