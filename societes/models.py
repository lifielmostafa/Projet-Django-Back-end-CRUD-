from django.db import models



class employee(models.Model):
    cin_employee = models.CharField(max_length=200)
    nom_employee = models.CharField(max_length=200)
    prenom_employee = models.CharField(max_length=200)
    spécialité_employee = models.CharField(max_length=200)
    salaire_employee=models.FloatField()
    owner = models.ForeignKey(
        'auth.User',
        related_name='employee',
        on_delete=models.CASCADE,
        null=True
    )




class projet(models.Model):
    titre_projet = models.CharField(max_length=200)
    date_debut_projet= models.DateTimeField()
    date_fin_projet= models.DateTimeField()
    budjet_projet=models.FloatField()
    type_projet= models.CharField(max_length=200)
    employe=models.ManyToManyField(employee)
    owner = models.ForeignKey(
        'auth.User',
        related_name='projet',
        on_delete=models.CASCADE,
        null=True
    )
    