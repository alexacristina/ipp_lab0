from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, QueryDict, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from models import Client, AccessToken
from rest_framework.views import APIView
import json

def get(request):
	if request.method == 'GET':
		return HttpResponse("")
	elif request.method == 'POST':
		return HttpResponse("")

class Register(APIView):

	def get(self, request):
		data =json.loads(list(request.GET)[0].replace('\'', ''))
		register_output = { 'code': -1 }
		u = authenticate(username=data['name_surname'], password=data['pass'])
		if u is not None:
		 	register_output['code'] = 1
			return JsonResponse(register_output)
		else:
			u = User()
			u.email = data['email']
			u.username = data['name_surname']
			u.set_password(data['pass'])
			register_output['code'] = 0 
			u.save()
			client = Client(client_id=data['client_id'])
			client.save()
			access_token = AccessToken(user=u, client=client)
			access_token.generate_token()
			access_token.save()
			register_output.update({'token' : access_token.token})
			return JsonResponse(register_output)

class Login(APIView):
	def get(self, request):
		data = json.loads(list(request.GET)[0].replace('\'', ''))
		user = authenticate(username=data['name_surname'], password=data['pass'])
		login_output = { 'code': -1}
		if user is not None:
			login_output['code'] = 0
			login(request, user)
			client = Client.objects.filter(client_id=data['client_id'])
			print client
			access_token = AccessToken.objects.filter(client = client, user = user).first()
			print access_token
			login_output.update({'token':access_token.token})
			return JsonResponse(login_output)
		else:
			login_output['code'] = 2
			return JsonResponse(login_output)


class GetLastLogin(APIView):
	def get(self, request):
		data = json.loads(list(request.GET)[0].replace('\'', ''))
		user = User.objects.filter(username = data['name_surname']).first()
		login_output = { 'code': -1}
		if user is not None:
			login_output['code'] = 0
			client = Client.objects.filter(client_id=data['client_id']).first()
			print client
			access_token = AccessToken.objects.filter(client = client, user = user).first()
			print data['token']
			print access_token.token
			if access_token.token == data['token']:
				
				user_last_login = user.last_login
				print user_last_login
				login_output.update({'last_login' : user.last_login})
				return JsonResponse(login_output)
			else:
				login_output['code'] = 3
				return JsonResponse(login_output)
		else:
			login_output['code'] = 2
			return JsonResponse(login_output)
