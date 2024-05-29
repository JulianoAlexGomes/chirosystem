from django.db import models

class cadastro_patologias(models.Model):
	id = models.AutoField(primary_key=True)
	patologia = models.TextField(max_length=255)
	sintomas = models.TextField(max_length=255)
	observacoes = models.TextField(max_length=255)