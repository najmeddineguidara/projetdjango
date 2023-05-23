import mailbox
import mailcap
from django.conf import settings
from django.shortcuts import render
from django.views.generic import *
from django.shortcuts import get_object_or_404
from ArtyProd.models import Detail,Personnel, Projet,Service,Equipe
from .forms import EquipeForm, PersonnelForm, ProjetForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.core.mail import send_mail
from django.core import mail
from django.core.mail.message import EmailMessage
from .forms import  DemandeProjetEditForm, DemandeProjetForm,  PersonnelForm, ProjetForm, ServiceForm
from .models import Client, DemandeProjet, Equipe, Projet, Service, Personnel
import socket
#--------------------------------------------------DEMANDE PROJETS------------------------------------------------------------------

def demande_projet(request):
    if request.method == 'POST':
        form = DemandeProjetForm(request.POST, request.FILES)
        if form.is_valid():
            demande_projet = form.save(commit=False)
            if request.user.is_authenticated:
                client = Client.objects.get(user=request.user)
                demande_projet.client = client
                demande_projet.save()
                messages.success(request, 'Votre demande de projet a été soumise avec succès.')
                return redirect('projet')
            else:
                messages.error(request, 'Vous devez être connecté pour soumettre une demande de projet.')
    else:
        form = DemandeProjetForm()
    return render(request, 'demande_projet.html', {'form': form})

def demande_projet_list(request):
    demandes_projet = DemandeProjet.objects.all()
    return render(request, 'demande_projet_list.html', {'demandes_projet': demandes_projet})


#---------------------------------------------------CRUD DEMANDE PROJET-----------------------------------------------------------------
def modifier_demande_projet(request, demande_projet_id):
    demande_projet = get_object_or_404(DemandeProjet, id=demande_projet_id)
    if request.method == 'POST':
        form = DemandeProjetEditForm(request.POST, instance=demande_projet)
        if form.is_valid():
            form.save()
            return redirect('demande_projet_list')
    else:
        form = DemandeProjetEditForm(instance=demande_projet)
    return render(request, 'ArtyProd/demandeprojet/modifier_demande_projet.html', {'form': form})

def supprimer_demande_projet(request, demande_projet_id):
    demande_projet = get_object_or_404(DemandeProjet, id=demande_projet_id)
    demande_projet.delete()
    return redirect('demande_projet_list')

#-----------------------------------------------CONTACT--------------------------------------------------------------------------
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        message_body = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"

        send_mail(
            'Contact Form Submission',
            message_body,
            settings.DEFAULT_FROM_EMAIL,
            ['najmeddineguidara71@gmail.com'],
            fail_silently=False,
        )
        return render(request, 'ArtyProd/contact/contact.html', {'success': True})
    
    return render(request, 'ArtyProd/contact/contact.html')






class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Welcome {username}, your account has been created successfully!')
            return redirect('home')
        else:
            return render(request, 'registration/register.html', {'form': form})

def TtPersonnel(request):
        personnels= Personnel.objects.all()
        context={'personnels':personnels}
        return render( request,'personnels/personnels.html',context )

def personnel(request):
       
    if request.method == "POST":
        form = PersonnelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            personnels = Personnel.objects.all()
            return render(request, 'personnels/personnels.html', {'personnels': personnels})
    else:
        form = PersonnelForm()
    personnels = Personnel.objects.all()
    return render(request, 'personnels/create_prs.html', {'form': form, 'personnels': personnels})




def delete_personnel(request, pk):
    msg = get_object_or_404(Personnel, pk=pk)
    if request.method == 'POST':
        msg.delete()
        return redirect('TtPersonnel')
    return render(request, 'personnels/delete_prs.html', {'msg': msg})

def detail_personnel(request, prs_id):
    personnel = get_object_or_404(Personnel, id=prs_id)
    context = {'personnel': personnel}
    return render(request, 'personnels/detail_prs.html', context)


def edit_personnel(request, pk):
    personnel = get_object_or_404(Personnel, pk=pk)
    if request.method == 'POST':
        form = PersonnelForm(request.POST, request.FILES, instance=personnel)
        if form.is_valid():
            form.save()
            return redirect('TtPersonnel')
    else:
        form = PersonnelForm(instance=personnel)
  
  
    return render(request, 'personnels/edit_prs.html', {'form': form})

def TtProjet(request):
        projets= Projet.objects.all()
        context={'projets':projets}
        return render( request,'projets/projets.html',context )

def projet(request):
       if request.method == "POST" :
         form = ProjetForm(request.POST,request.FILES)
         if form.is_valid():
              form.save() 
              projets=Projet.objects.all()

              return render(request,'projets/projets.html',{'projets':projets})
       else : 
            form = ProjetForm() #créer formulaire vide 
            projets=Projet.objects.all()
            return render(request,'projets/create_projets.html',{'form':form,'projets':projets})

def delete_projet(request, proj_id):
    prj = get_object_or_404(Projet, id=proj_id)
    if request.method == 'POST':
        prj.delete()
        return redirect('TtProjet')
    return render(request, 'projets/delete_projets.html', {'prj': prj})

def detail_projet(request, proj_id):
    projet = get_object_or_404(Projet, id=proj_id)
    context = {'projet': projet}
    return render(request, 'projets/detail_projets.html', context)


def edit_projet(request, proj_id):
    projet = get_object_or_404(Projet, id=proj_id)
    if request.method == 'POST':
        form = ProjetForm(request.POST, request.FILES, instance=projet)
        if form.is_valid():
            form.save()
            return redirect('TtProjet')
    else:
        form = ProjetForm(instance=projet)
    return render(request, 'projets/edit_projets.html', {'form': form})


def create_equipe(request):
     if request.method == "POST" :
         form = EquipeForm(request.POST)
         if form.is_valid():
              form.save() 
              equipes=Equipe.objects.all()
              
              return render(request,'equipes/equipes.html',{'equipes':equipes})
     else : 
            form = EquipeForm() #créer formulaire vide 
            equipes=Equipe.objects.all()
            return render(request,'equipes/create_equipe.html',{'form':form,'equipes':equipes})


def detail_equipe(request, equipe_id):
    equipe = get_object_or_404(Equipe, id=equipe_id)
    context = {'equipe': equipe}
    return render(request, 'equipes/detail_equipe.html', context)


def edit_equipe(request, equipe_id):
    equipe = get_object_or_404(Equipe, id=equipe_id)
    if request.method == 'POST':
        form = EquipeForm(request.POST, instance=equipe)
        if form.is_valid():
            form.save()
            return redirect('list_equipes')
    else:
        form = EquipeForm(instance=equipe)
        return render(request, 'equipes/edit_equipe.html',{'form': form})


def delete_equipe(request, equipe_id):
    equipe = get_object_or_404(Equipe, id=equipe_id)
    if request.method == 'POST':
        equipe.delete()
        return redirect('list_equipes')
    return render(request, 'equipes/delete_equipe.html', {'equipe': equipe})


def list_equipes(request):
    equipes = Equipe.objects.all()
    context = {'equipes': equipes}
    return render(request, 'equipes/equipes.html', context)

from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact, Service
from .forms import ServiceForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Service
from .forms import ServiceForm

def TtService(request):
    services = Service.objects.all()
    return render(request, 'service/service_list.html', {'services': services})



def create_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('TtService')
    else:
        form = ServiceForm()
    return render(request, 'service/service_create.html', {'form': form})

def detail_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'service/service_detail.html', {'service': service})

def edit_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service/detail_service', service_id=service_id)
    else:
        form = ServiceForm(instance=service)
    return render(request, 'service/service_edit.html', {'form': form, 'service': service})

def delete_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        service.delete()
        return redirect('TtService')
    return render(request, 'service/service_delete.html', {'service': service})









def create_equipe(request):
     if request.method == "POST" :
         form = EquipeForm(request.POST)
         if form.is_valid():
              form.save() 
              equipes=Equipe.objects.all()
              
              return render(request,'equipes/equipes.html',{'equipes':equipes})
     else : 
            form = EquipeForm() #créer formulaire vide 
            equipes=Equipe.objects.all()
            return render(request,'equipes/create_equipe.html',{'form':form,'equipes':equipes})




class DetailListView(ListView):
    model = Detail
    template_name = 'detail_list.html'
    context_object_name = 'details'


class DetailCreateView(LoginRequiredMixin, CreateView):
    model = Detail
    fields = ['fichier', 'service']
    template_name = 'detail_creatr.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class DetailUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Detail
    fields = ['fichier', 'service']
    template_name = 'myapp/detail_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        detail = self.get_object()
        if self.request.user == detail.created_by:
            return True
        return False


# Views for Equipe model




class EquipeDetailView(DetailView):
    model = Equipe


class EquipeCreateView(LoginRequiredMixin, CreateView):
    model = Equipe
    fields = ['nom', 'membres']
    template_name = 'create_equipe.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class EquipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Equipe
    fields = ['nom', 'membres']
    template_name = 'edit_equipe.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        equipe = self.get_object()
        if self.request.user == equipe.created_by:
            return True
        return False

def indexA(request):
    return render(request, 'about.html')


from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import ClientCreationForm

def inscription_client(request):
    if request.method == 'POST':
        form = ClientCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('indexA')
    else:
        form = ClientCreationForm()
    return render(request, 'inscription_client.html', {'form': form})




from django.shortcuts import render, redirect
from .forms import DemandeProjetForm

def demande_projet(request):
    if request.method == 'POST':
        form = DemandeProjetForm(request.POST)
        if form.is_valid():
            form.save()
            # Faites les actions nécessaires après la sauvegarde du projet
            return redirect('indexA')  # Redirige vers la page d'accueil après la soumission réussie
    else:
        form = DemandeProjetForm()
    
    context = {'form': form}
    return render(request, 'demandeprojet.html', context)
