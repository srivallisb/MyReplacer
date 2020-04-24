from django.db import models

class Replacewords(models.Model):
	title=models.CharField(max_length=50,null=True,blank=True)
	paragraph=models.TextField(null=True,blank=True)
	substring_to_be_replaced=models.CharField(max_length=50,null=True,blank=True)
	replace_word=models.CharField(max_length=50,null=True,blank=True)
	new_para=models.TextField(null=True,blank=True)
	def __str__(self):
		return self.title