from django.db import models

# Create your models here.
class user(models.Model):
	name=models.CharField(max_length=30)
	latitude= models.FloatField() 
	longitude= models.FloatField() 
	time_of_record=models.DateTimeField(auto_now_add=True)
	date_of_birth=models.DateField()
	blood_type=models.CharField(max_length=30)
	gender=models.CharField(max_length=30)
	phn_num=models.CharField(max_length=10)
	id_proof=models.ImageField(upload_to ='uploads/', null=True, blank=True)
	list_infectious_diseases= models.CharField(max_length=100, null=True, blank=True)
	flag= models.BooleanField()

	def __str__(self):
		return self.name

class blood_request(models.Model):
	latitude= models.FloatField() 
	longitude= models.FloatField() 
	time_of_record=models.DateTimeField(auto_now_add=True)
	blood_type=models.CharField(max_length=30)
	recipient=models.ForeignKey(user, on_delete=models.DO_NOTHING, related_name='recipient')
	donor=models.ForeignKey(user, on_delete=models.DO_NOTHING, related_name='donor')
	def __str__(self):
		return self.blood_type