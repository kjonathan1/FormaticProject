from django.urls import path, include
from training import views

urlpatterns = [
    path('list-session/', views.listSession, name='list-session'),
    path('create-session/', views.createSession, name='create-session'),
    path('update-session/<str:pk>/', views.updateSession, name='update-session'),
    path('show-session/<str:pk>/', views.showSession, name='show-session'),
    path('delete-session/<str:pk>/', views.deleteSession, name='delete-session'),

    path('list-module/', views.listModule, name='list-module'),
    path('create-module/', views.createModule, name='create-module'),
    path('update-module/<str:pk>/', views.updateModule, name='update-module'),
    path('show-module/<str:pk>/', views.showModule, name='show-module'),
    path('delete-module/<str:pk>/', views.deleteModule, name='delete-module'),

    path('list-inscription/', views.listInscription, name='list-inscription'),
    path('create-inscription/<str:pk>/', views.createInscription, name='create-inscription'),
    path('update-inscription/<str:pk>/', views.updateInscription, name='update-inscription'),
    path('show-inscription/<str:pk>/', views.showInscription, name='show-inscription'),
    path('delete-inscription/<str:pk>/', views.deleteInscription, name='delete-inscription'),

    path('list-etudiant/', views.listEtudiant, name='list-etudiant'),
    path('create-etudiant/', views.createEtudiant, name='create-etudiant'),
    path('update-etudiant/<str:pk>/', views.updateEtudiant, name='update-etudiant'),
    path('show-etudiant/<str:pk>/', views.showEtudiant, name='show-etudiant'),
    path('delete-etudiant/<str:pk>/', views.deleteEtudiant, name='delete-etudiant'),



    path('inscrire-etudiant/<str:pk>/', views.createInscription, name='inscrire-etudiant'),
]