from rest_framework import serializers
from  .models import employee,projet




class EmployeeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = employee
        fields = ['id','cin_employee','nom_employee','prenom_employee','spécialité_employee','salaire_employee','owner']
        depth = 1
class ProjetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model =projet
        fields =['id','titre_projet','date_debut_projet','date_fin_projet','budjet_projet','type_projet','employe','owner']
        depth = 1 