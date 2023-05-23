from django.forms import IntegerField
from rest_framework.serializers import ModelSerializer
from ArtyProd.models import Client, DemandeProjet, Personnel, Equipe, Projet, Service
class DemandeProjetSerializer(ModelSerializer):
    class Meta:
        model = DemandeProjet
        fields = ['id', 'libelle', 'description', 'date_demande', 'service','equipe','client','statut']
