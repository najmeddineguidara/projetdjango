from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Personnel, Projet, Service, Detail, Equipe
from .models import DemandeProjet
class PersonnelForm(forms.ModelForm):
     class Meta : 
        model = Personnel
        fields = "__all__"

class ProjetForm(forms.ModelForm):
     class Meta : 
        model = Projet
        fields = "__all__" #pour tous les champs de la table


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'


class DetailForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = '__all__'


class EquipeForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = '__all__'
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + \
            ('first_name', 'last_name', 'email')

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ClientCreationForm(UserCreationForm):
    nom = forms.CharField(max_length=255)
    adresse = forms.CharField(max_length=255)
    telephone = forms.CharField(max_length=255)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'nom', 'adresse', 'telephone', 'email']
class DemandeProjetForm(forms.ModelForm):
    class Meta:
        model = DemandeProjet
        exclude = ['client', 'date_demande', 'statut', 'equipe']
        labels = {
            'libelle': 'Libellé',
            'description': 'Description',
            'service': 'Service',
        } 

class DemandeProjetEditForm(forms.ModelForm):
    class Meta:
        model = DemandeProjet
        exclude = ['client', 'libelle', 'description', 'service', 'date_demande' ]
        labels = {
            'statut': 'Statut',
            'equipe': 'Equipe',
        } 
