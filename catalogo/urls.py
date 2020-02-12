from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ricette/manage/', views.manageRicette, name='rmanage'),
    path('ricette/create/', views.createRicetta.as_view(), name='rcreate'),
    path('ricette/<int:pk>/delete/', views.deleteRicetta.as_view(), name='rdelete'),
    path('ricette/<int:pk>/update/', views.updateRicetta.as_view(), name='rupdate'),
    path('ricette/<int:pk>/show/', views.showRicetta, name='rshow'),
    path('ricette/search/', views.searchRicetta.as_view(), name='rsearch'),
    path('ingredienti/manage/', views.manageIngredienti, name='imanage'),
    path('ingredienti/create/', views.createIngrediente.as_view(), name='icreate'),
    path('ingredienti/<int:pk>/delete/', views.deleteIngrediente.as_view(), name='idelete'),
    path('ingredienti/<int:pk>/update/', views.updateIngrediente.as_view(), name='iupdate'),
    path('ricette/<int:pk>/ingrediente/add', views.createIngredienteToRicetta.as_view(), name='ircreate'),
    path('ricette/<int:pk>/ingrediente/del', views.deleteIngrediente.as_view(), name='irdelete'),
    path('utenti/manage', views.manageUtenti, name='umanage'),
    path('utenti/create', views.createUser.as_view(), name='ucreate'),
    path('utenti/<int:pk>/delete', views.deleteUser.as_view(), name='udelete'),
    path('utenti/<int:pk>/update', views.updateUser.as_view(), name='uupdate'),
]
