from django.utils import  timezone

from django.contrib.auth.models import  User
from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse
import datetime

# Create your models here.

from django.contrib.auth.models import User, Group

class Personnel(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100, default='')
    date_naissance = models.DateField(default=datetime.date.today)
    photo = models.ImageField(upload_to='photosProfil/', blank=True, null=True)
    cv = models.FileField(upload_to='cv/', blank=True, null=True)
    date_affectation = models.DateField(null=True, default=datetime.date.today)
    profil_linkedin_ou_site_personnel = models.URLField(blank=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"


    

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255, default="")
    adresse = models.CharField(max_length=255, default="")
    telephone = models.CharField(max_length=255, default="")
    email = models.EmailField(max_length=255, default="")
    Img = models.ImageField(upload_to='media/', null=True, blank=True)

    def __str__(self):
        return f'{self.user.username}, {self.adresse}, {self.telephone}'

    def save(self, *args, **kwargs):
        # Vérifier si le groupe "Client" existe, sinon le créer
        group, created = Group.objects.get_or_create(name='Client')
        self.user.groups.add(group)
        super().save(*args, **kwargs)


class DemandeProjet(models.Model):
    libelle = models.CharField(max_length=50)
    description = models.TextField()
    date_demande = models.DateTimeField(auto_now_add=True)
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    equipe = models.ForeignKey('Equipe', on_delete=models.CASCADE, null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    STATUT_CHOICES = [
        ('En attente', 'En attente'),
        ('En cours', 'En cours'),
        ('Terminé', 'Terminé')
    ]
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES)
    
    def __str__(self):
        return self.libelle
    









class Projet(models.Model):
    libelle = models.CharField(max_length=50, default='')  # Définir la valeur par défaut à une chaîne vide ou une autre valeur appropriée
    description = models.TextField(default='')
    date_debut = models.DateField(default=datetime.date.today)
    date_fin = models.DateField(default=datetime.date.today)
    acheve = models.BooleanField(default=False)
    image = models.ImageField(upload_to='media/', blank=True)
    service = models.ForeignKey('Service', on_delete=models.CASCADE, null=True, blank=True)
    equipe = models.ForeignKey('Equipe', on_delete=models.CASCADE, null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.libelle



class Service(models.Model):
    TYPE_CHOICES = [
        ('Design Graphique', 'Design Graphique'),
        ('Design Web', 'Design Web'),
        ('SC', 'Scénarisation'),
    ]

    nom = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    image = models.ImageField( null=True, blank=True)

    def str(self):
        return self.nom

class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
class Detail(models.Model):
    fichier = models.FileField(upload_to='media/')

    def __str__(self):
        return f'{self.fichier}'



class Equipe(models.Model):
    nom = models.CharField(max_length=25)
    membres = models.ManyToManyField(Personnel)
    
    
    def __str__(self):
        return f'{self.nom}, {self.membres}'
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phoneNumber=models.CharField(max_length=12)
    description=models.TextField()
    def __str__(self) :
  
        return f'Message from {self.name}'
    
class Panier(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_ajout = models.DateTimeField(default=timezone.now)    
    quantite = models.IntegerField(default=1)
    def total_prix(self):
        return sum([f.prix for f in self.formations.all() if f.prix])