from django.shortcuts import render
from django.template import RequestContext
import json
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import datetime

from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import check_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import *

import random
import string
from django.conf import settings

import braintree
braintree.Configuration.configure(braintree.Environment.Sandbox,
							  merchant_id=settings.BRAINTREE_MERCHANT,
							  public_key=settings.BRAINTREE_PUBLIC_KEY,
							  private_key=settings.BRAINTREE_PRIVATE_KEY)


def index(request):
	context={}
	return render(request, 'index.html', contex)
def subscription(request):
	rg = request.POST.get
	message = ''
	token = None
	customer_id = None
	if request.POST:
		if rg('fname') and rg('lname') and rg('cnumber') and rg('cvv') and rg('year') and rg('month'):
			print rg('fname'),rg('lname'), rg('cnumber') , rg('cvv') , rg('year') , rg('month')

			# number = rg('cnumber')
			# expiration_date = rg('year')/rg('month')

			client_token = braintree.ClientToken.generate()


			print client_token

			# result = braintree.Customer.create({
			#     "credit_card": {
			#         "number": "4111111111111111",
			#         "expiration_date": "12/16"
			#       }
			#   })

			# print result

			# print result.customer.payment_method_nonce

			# result = braintree.Subscription.create({
			#     "payment_method_token": result.credit_cards[0].token,
			#     "plan_id": "my_plan_id"
			#   })

			# print 
			# if result.is_success:
			#   print "Subscription success!"

			# customer = braintree.Customer.create({
			#     "credit_card": {
			#         "number":number,
			#         "expiration_date":expiration_date,
			#     }
			# })

			# payment_method_token = client.customer.credit_cards[0].token



			# token = client_token()
			# payment_token_id = generate_payment_token(token)
			# print payment_token_id
		else:
			print "enter valid page"
			message = 'Please enter valid form'
			varibles ={'message':message}
			return render(request, 'index.html', varibles)

def client_token():
	client_token = braintree.ClientToken.generate()
	return client_token

def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def generate_payment_token(token):
	payment_token_nonce = braintree.PaymentMethod.create({
	"customer_id": token,
	"payment_method_nonce": nonce_from_the_client
	})
@login_required
def dashboard(request):
	varibles ={}
	return render(request, 'dashboard.html', varibles)

def registraion(request):
	rg = request.POST.get
	message = ''
	if request.POST:
		print "hello post here"
		if rg('first_name') and rg('last_name') and rg('email') and rg('password'):
			email = rg('email')
			if User.objects.filter(email=email) or  User.objects.filter(username=email):
				message = 'Please enter valid email already exist'
				varibles ={'message':message}
				return render(request, 'registration/signup.html', varibles)
			else:
				staff=Staff()
				staff.username = email
				staff.email = email
				staff.first_name = rg('first_name')
				staff.last_name = rg('last_name')
				staff.set_password(rg('password'))
				staff.save()
				user=authenticate(username=staff.username,password=rg('password'))
				if user:
					login(request,user)
					subject = 'Account created successfully' 
					return HttpResponseRedirect(reverse('dashboard',))


		else:
			print "something is missing please look back"

			message = 'Please enter valid form'

			varibles ={'message':message}
			return render(request, 'registration/signup.html', varibles)
	else:
		varibles ={}
		return render(request, 'registration/login.html')


@login_required
@csrf_exempt
def checkout(request):
	rg = request.POST.get

	amount =  request.POST.get('prise')

	print "============"

	print amount

	user = Staff.objects.get(id=request.user.id)
	a_customer_id = ''
	if not user.customer_id:
		result = braintree.Customer.create({
		    "first_name": user.first_name,
		    "last_name": user.last_name,
		    "company": "Braintree",
		    "email": user.email,
		    "phone": "312.555.1234",
		    "fax": "614.555.5678",
		    "website": "www.example.com"
			})
		if result.is_success:
			user.customer_id = result.customer.id
			user.save()
			a_customer_id = user.customer_id
	else:
		a_customer_id = user.customer_id
	if not user.client_token:
		client_token = client_token = braintree.ClientToken.generate({
			    "customer_id": a_customer_id
			})
		user.client_token = client_token
		user.save()
	else:
		client_token = user.client_token

	varibles ={'amount':amount,'client_token':client_token}
	return render(request, 'checkout.html',varibles)


@login_required
@csrf_exempt
def payment(request):
	if request.POST:
		if request.POST.get("payment_method_nonce"):
			nonce_from_the_client =  request.POST.get("payment_method_nonce")
			staff = Staff.objects.get(id=request.user.id)
			sub = Subscription()
			sub.staff = staff
			sub.payment_nonce = nonce_from_the_client
			sub.amount = request.POST.get("amount")
			sub.save()
			result = braintree.Transaction.sale({
		    "amount": sub.amount,
		    "payment_method_nonce": sub.payment_nonce
			})
			transaction_id =  result.transaction.id
			sub.txnid = transaction_id
			sub.save()
			message = ''
			if result.is_success:
				sub.result = True
				sub.save()
				message =  'Transaction successfully completed'+' : '+ transaction_id
				varibles ={'message':message}
				return render(request, 'success.html',varibles)
			else:
				message = 'Error Transaction Faild'

				varibles ={'message':message,}
				return render(request, 'checkout.html',varibles)
		else:
			message = 'No transaction'

			varibles ={'message':message,}
			return render(request, 'checkout.html',varibles)
			






























