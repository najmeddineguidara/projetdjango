import statistics
from django.contrib import admin
from django.urls import path
from.import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
urlpatterns = [

    #contact
    path('contact',views.contact,name='contact'),
    #--------------------------------DEMANDE PROJET---------------------------------------
    path('demande_projet/', views.demande_projet, name='demande_projet'),
    path('demande_projet_list/', views.demande_projet_list, name='demande_projet_list'),
    path('demande_projet/<int:demande_projet_id>/edit/', views.modifier_demande_projet, name='modifier_demande_projet'),
    path('demande_projet/<int:demande_projet_id>/delete/', views.supprimer_demande_projet, name='supprimer_demande_projet'),

    path('service/', views.Service, name='service'),
    path('contact/', views.contact, name='contact'),
    


    path('personnel/', views.personnel, name='personnel'),
    path('TtPersonnel/', views.TtPersonnel, name='TtPersonnel'),
    path('deletePersonnel/<int:pk>/', views.delete_personnel, name='delete_personnel'),
    path('Personnel/<int:prs_id>/', views.detail_personnel, name='detail_personnel'),
    path('editPersonnem/<int:pk>/', views.edit_personnel, name='edit_personnel'),
    
    path('Projets', views.TtProjet, name='TtProjet'),
    path('createProjet/', views.projet, name='projet'),
    path('<int:proj_id>/detailProjet/', views.detail_projet, name='detail_projet'),
    path('<int:proj_id>/editProjet/', views.edit_projet, name='edit_projet'),
    path('<int:proj_id>/deleteProjet/', views.delete_projet, name='delete_projet'),

    path('Equipes', views.list_equipes, name='list_equipes'),
    path('createEquipe/', views.create_equipe, name='create_equipe'),
    path('<int:equipe_id>/detail_equipe', views.detail_equipe, name='detail_equipe'),
    path('<int:equipe_id>/edit_equipe/', views.edit_equipe, name='edit_equipe'),
    path('<int:equipe_id>/delete_equipe/', views.delete_equipe, name='delete_equipe'),
    
   
    path('services/', views.TtService, name='TtService'),
    path('createService/', views.create_service, name='create_service'),
    path('<int:service_id>/detailService/', views.detail_service, name='detail_service'),
    path('<int:service_id>/editService/', views.edit_service, name='edit_service'),
    path('<int:service_id>/deleteService/', views.delete_service, name='delete_service'),


    path('', views.indexA, name='indexA'),
    path('inscription_client/', views.inscription_client, name='inscription_client'),
    #detail
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name = 'logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
