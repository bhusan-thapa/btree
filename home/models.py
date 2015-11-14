from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Staff(User):
	client_token = models.TextField(verbose_name=u'client token', max_length=500)
	payment_once = models.CharField(max_length=100,null=True,blank=True)
	customer_id = models.CharField(max_length=25,null=True,blank=True)
	payment_mode = models.BooleanField(default=False)

	def __str__(self):
		return self.first_name 

class Subscription(models.Model):
	staff = models.ForeignKey(Staff,related_name='subscription')
	payment_nonce = models.CharField(max_length=100,null=True,blank=True)
	amount = models.CharField(max_length=100,null=True,blank=True)
	txnid = models.CharField(max_length=25,null=True,blank=True)
	result = models.BooleanField(default=False)


	def __str__(self):
		return self.staff.first_name + ' : ' + str(self.amount)




	