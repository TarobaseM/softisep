from django.contrib import admin
from django.urls import path, include
from softisepapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),

    # Page d'accueil
    path('', views.index, name='index'),

    # Vue pour afficher les détails d'un logiciel
    path('logiciel/<str:logiciel_name>/', views.logiciel_view, name='logiciel_view'),

    # URLs pour l'authentification
    path('accounts/', include('allauth.urls')),

    # Vue pour afficher les cours de l'utilisateur connecté
    path('my_courses/', views.my_courses, name='my_courses'),
]

# Ajouter les URLs pour les fichiers statiques en mode DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
