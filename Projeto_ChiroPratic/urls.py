from django.urls import path
from app_chiropratic import views

urlpatterns = [
    path('', views.pagina_home, name='home'),
    path('patologias/', views.patologia, name='patologias'),
    path('lista_patologias/', views.lista_patologias, name='lista_patologias'),
    path('cadastro_patologias/', views.cadastro_patologia, name='cadastro_patologias'),
    path('delete_patologia/<int:id>/', views.delete_patologia, name='delete_patologia'),
    path('edit_patologia/<int:id>/', views.edit_patologia, name='edit_patologia'),
]
