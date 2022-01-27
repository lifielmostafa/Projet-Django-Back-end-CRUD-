
from  django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EmployeeSerializer
from .serializers import ProjetSerializer
from .models import employee
from .models import projet
from rest_framework import generics
from rest_framework import mixins
from django.contrib.auth import get_user_model

User=get_user_model()

class EmployeGenericApi(generics.GenericAPIView,mixins.ListModelMixin,
                     mixins.DestroyModelMixin,mixins.UpdateModelMixin,
                     mixins.CreateModelMixin,mixins.RetrieveModelMixin):
    serializer_class=EmployeeSerializer
    queryset=employee.objects.all()
    lookup_field='id'
    def get(self,request,id=None):
         if id:
             return self.retrieve(request)
         else:
             return self.list(request)
#--------------------------------------------
    def post(self,request):
        data = request.data
        superuser = User.objects.filter(is_superuser=True,username=data["owner"]).first()
        new_employee=employee.objects.create(cin_employee=data["cin_employee"],nom_employee=data["nom_employee"],
       prenom_employee=data["prenom_employee"],spécialité_employee=data["spécialité_employee"],salaire_employee=data["salaire_employee"],owner=superuser)
        new_employee.save()
        serializer = EmployeeSerializer(new_employee)
        return Response(serializer.data)
       
#--------------------------------------------
    def put(self,request,id=None):
        return self.update(request,id)
#---------------------------------------------
    def delete(self,request,id):
        return self.destroy(request,id)
class ProjetGenericApi(generics.GenericAPIView,mixins.ListModelMixin,
                     mixins.DestroyModelMixin,mixins.UpdateModelMixin,
                     mixins.CreateModelMixin,mixins.RetrieveModelMixin):
    serializer_class=ProjetSerializer
    queryset=projet.objects.all()
    lookup_field='id'
    def get(self,request,id=None):
         if id:
             return self.retrieve(request)
         else:
             return self.list(request)
#--------------------------------------------
    def post(self,request):

        data = request.data
        superuser = User.objects.filter(is_superuser=True,username=data["owner"]).first()
        new_projet=projet.objects.create(titre_projet=data["titre_projet"],date_debut_projet=data["date_debut_projet"],
        date_fin_projet=data["date_fin_projet"],budjet_projet=data["budjet_projet"],type_projet=data["type_projet"],owner=superuser)
        new_projet.save()
        for emp in data["employe"]:
            employe_obj=employee.objects.get(nom_employee=emp["nom_employee"])
            new_projet.employe.add(employe_obj)
        serializer = ProjetSerializer(new_projet)
        return Response(serializer.data)

#--------------------------------------------
    def put(self,request,id=None):
        return self.update(request,id)
#---------------------------------------------
    def delete(self,request,id):
        return self.destroy(request,id)
                
class GetByCin(generics.RetrieveAPIView):
    serializer_class=EmployeeSerializer
    queryset=employee.objects.all()
    lookup_field='cin_employee'
    def get(self,request,cin_employee):
        return self.retrieve(request)

       
class GetByTitre_projet(generics.RetrieveAPIView):
    serializer_class=ProjetSerializer
    queryset=projet.objects.all()
    lookup_field='titre_projet'
    def get(self,request,titre_projet):
        return self.retrieve(request)
@api_view(['GET'])
def emp_projet(request,id):
    prjt = projet.objects.filter(employe__id=id)
    serializer = ProjetSerializer(prjt,many=True)
    return Response(serializer.data)

