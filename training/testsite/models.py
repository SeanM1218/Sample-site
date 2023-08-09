from django.db import models

# Create your models here.
class patient(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class illness(models.Model):
    patient = models.ForeignKey(patient, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    treated = models.BooleanField()

    def __str__(self):
        return self.text
