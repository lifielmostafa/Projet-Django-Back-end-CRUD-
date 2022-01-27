from django.urls import path
from . import views
from .views import EmployeGenericApi
from .views import ProjetGenericApi
from .views import GetByCin
from .views import GetByTitre_projet
from .views import emp_projet



urlpatterns = [
    path('generic/employee/',EmployeGenericApi.as_view()),
    path('generic/employee/<int:id>/',EmployeGenericApi.as_view()),
    path('generic/projet/',ProjetGenericApi.as_view()),
    path('generic/projet/<int:id>/',ProjetGenericApi.as_view()),
    path('generic/employee/<cin_employee>/',GetByCin.as_view()),
    path('generic/projet/<titre_projet>/',GetByTitre_projet.as_view()),
    path('join/<int:id>/',views.emp_projet),
    
    

]