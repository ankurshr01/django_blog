from django.db import models
#from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=1000)
	date=models.DateTimeField()
	image=models.ImageField(upload_to='media/')
	images1=models.ImageField(upload_to='media/')	
	body=models.TextField()
	author=models.TextField(max_length=20)

	def __str__(self):
		  return self.title  
 

	def pub_date_pretty(self):
		   return self.date.strftime('%b %d %Y')
		
	def summary(self):
		   return self.body[:300]	



