from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def studlist(request):
    response=requests.get('https://jsonplaceholder.typicode.com/users')
    print("----------------++++++++++++++++++++---------------------")
    return HttpResponse(response.json())

