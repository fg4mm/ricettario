from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from catalogo.models import Ricetta
from catalogo.models import Ingrediente
from catalogo.models import IngredientiRicette
from catalogo.models import User


# Create your views here.

#########################Ricette####################################

#TODO: dividire in pagine l'elenco delle ricette
def index(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            ricette = Ricetta.objects.all().order_by('-id')
        else:
            #filtro in base all'utente se l'utente non è superuser
            ricette = Ricetta.objects.all().order_by('-id').filter(autore=request.user)
    else:
        #Pubblico le ultime 5 ricette inserite nel database dagli utenti se un visitatore generico
            ricette = Ricetta.objects.all().order_by('-id')[:5]

    context = {
        'ricette': ricette,
    }

    return render(request, 'catalogo/index.html', context=context)


def showRicetta(request,pk=None):
    if pk:
          try:
                ricetta = Ricetta.objects.get(pk=pk)
          except:
                ricetta = None
          try:
                ingredienti = IngredientiRicette.objects.filter(ricetta=pk)
          except:
                ingredienti = None
    else:
          ricetta = None
          ingredienti = None

    context = {
            'ricetta': ricetta,
            'ingredienti': ingredienti,
    }

    return render(request, 'catalogo/show.html', context=context)


#Ricerca nei campi nome e descrizione delle ricette inserite

class searchRicetta(ListView):
    model = Ricetta
    template_name = 'catalogo/search.html'

    def get_queryset(self): 
        query = self.request.GET.get('q')

        return Ricetta.objects.filter(
            Q(nome__icontains=query) | Q(descrizione__icontains=query)
        )

        return object_list


@login_required
def manageRicette(request):

    if request.user.is_superuser:
        ricette = Ricetta.objects.all().order_by('-id')
    else:
        ricette = Ricetta.objects.all().order_by('-id').filter(autore=request.user)

    context = {
        'ricette': ricette,
    }

    return render(request, 'catalogo/index.html', context=context)


class createRicetta(LoginRequiredMixin,CreateView):
    model = Ricetta
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    fields = ["nome","tipo","difficolta","immagine","descrizione","nazionalita"]

    def get_success_url(self):
        return reverse_lazy('rmanage')

    def form_valid(self, form):
        form.instance.autore = self.request.user
        return super(createRicetta, self).form_valid(form)

class deleteRicetta(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Ricetta
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    success_url = reverse_lazy('rmanage')

    #Controllo che una ricetta sia cancellata solo dall'autore o dal superuser
    def test_func(self):
        pk = self.kwargs['pk']
        if pk:
            ricetta = Ricetta.objects.get(pk=pk)
            if ricetta.autore == self.request.user or self.request.user.is_superuser:
                return True
        else:
            return False

class updateRicetta(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Ricetta
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    fields = ["nome","tipo","difficolta","immagine","descrizione","nazionalita"]

    def get_success_url(self):
        return reverse_lazy('rmanage')

    def form_valid(self, form):
        form.instance.autore = self.request.user
        return super(updateRicetta, self).form_valid(form)

    #Controllo che una ricetta sia aggiornata solo dall'autore o dal superuser
    def test_func(self):
        pk = self.kwargs['pk']
        if pk:
            ricetta = Ricetta.objects.get(pk=pk)
            if ricetta.autore == self.request.user or self.request.user.is_superuser:
                return True
        else:
            return False


#########################Ingredienti################################

#Solo superuser può creare e gestire gli ingredienti per le ricette

@user_passes_test(lambda u: u.is_superuser)
def manageIngredienti(request):
    #Elenco tutti gli ingredienti nel database in una tabella con le opzioni Cancella/Modifica
    #TODO: dividire in pagine l'elenco
    try:
        ingredienti = Ingrediente.objects.all().order_by('nome')
    except:
        ingredienti = None

    context = {
        'ingredienti': ingredienti,
    }

    return render(request, 'catalogo/manage_ingredienti.html', context=context)

class createIngrediente(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Ingrediente
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    fields = ["nome","calorie"]

    def get_success_url(self):
        return reverse_lazy('imanage')

    #Solo il superuser può aggiungere gli ingredienti per le ricette
    def test_func(self):
            return self.request.user.is_superuser


class deleteIngrediente(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Ingrediente
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get_success_url(self):
        return reverse_lazy('imanage')

    #Solo il superuser può cancellare gli ingredienti per le ricette
    def test_func(self):
            return self.request.user.is_superuser


class updateIngrediente(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Ingrediente
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    fields = ["nome","calorie"]

    def get_success_url(self):
        return reverse_lazy('imanage')

    #Solo il superuser può aggiornare gli ingredienti per le ricette
    def test_func(self):
            return self.request.user.is_superuser


#########################Ingredienti->Ricetta#######################

#Associa un ingrediente a una ricetta per comporre una lista 
#di ingredienti e relative quantità 

class createIngredienteToRicetta(LoginRequiredMixin,CreateView):
    model = IngredientiRicette
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    fields = ["ingrediente","quantita"]
    
#Controllo che un utente aggiunga ingredienti solo alla proprie ricette
    def form_valid(self, form):
        pk = self.kwargs['pk']
        if  Ricetta.objects.get(pk=pk).autore == self.request.user:
            form.instance.ricetta = Ricetta(pk=pk)
            return super(createIngredienteToRicetta, self).form_valid(form)
        else:
            return super(createIngredienteToRicetta, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('rmanage')


class deleteIngredienteToRicetta(LoginRequiredMixin,CreateView):
    model = IngredientiRicette
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get_success_url(self):
        return reverse_lazy('rmanage')

    def form_valid(self, form):
        pk = self.kwargs['pk']
        if  Ricetta.objects.get(pk=pk).autore == self.request.user:
            form.instance.ricetta = Ricetta(pk=pk)
            return super(deleteIngredienteToRicetta, self).form_valid(form)
        else:
            return super(deleteIngredienteToRicetta, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('rmanage')



#########################Utenti#####################################

@user_passes_test(lambda u: u.is_superuser)
def manageUtenti(request):

    try:
        utenti = User.objects.all().order_by('email')
    except:
        utenti = None

    context = {
        'utenti': utenti,
    }

    return render(request, 'catalogo/user_manage.html', context=context)


class createUser(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = User
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    fields = ['email','first_name','last_name','birth_date','gender','password']

    def get_success_url(self):
        return reverse_lazy('umanage')

    #Solo il superuser può creare utenti
    def test_func(self):
            return self.request.user.is_superuser

    #genero una password valida utilizzando la funzione make_password
    def form_valid(self, form):
        pk = self.kwargs['pk']
        form.instance.password = make_password(form.instance.password)
        return super(updateUser, self).form_valid(form)



class deleteUser(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = User
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get_success_url(self):
        return reverse_lazy('umanage')

    #Solo il superuser può cancellare utenti
    def test_func(self):
            return self.request.user.is_superuser

class updateUser(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = User
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    fields = ['email','first_name','last_name','birth_date','gender','password']

    def get_success_url(self):
        return reverse_lazy('umanage')

    #Solo il superuser può aggiornare il profilo di un utente
    def test_func(self):
            return self.request.user.is_superuser

    #genero una password valida utilizzando la funzione make_password
    def form_valid(self, form):
        pk = self.kwargs['pk']
        form.instance.password = make_password(form.instance.password)
        return super(updateUser, self).form_valid(form)


