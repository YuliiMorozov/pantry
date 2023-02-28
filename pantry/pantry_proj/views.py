from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json

from .services import register_user, login_user

def index(request):
    return render(request, 'pantry_proj/index.html')

def contact(request):
    return render(request, 'pantry_proj/contact.html')

# def json(request):
#     info = {
#         'name': 'Yulii',
#         'username': '@yulii',
#         'age': '29'
#     }  

#     return JsonResponse(info)


@csrf_exempt
def sign_up(request):
    return register_user(request)

@csrf_exempt
def sign_in(request):
    return login_user(request)