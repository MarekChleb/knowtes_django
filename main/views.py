from django.shortcuts import render
from django.http import JsonResponse
from main.models import Knowte

# Create your views here.


def knowte(request):
  ret = {}
  id = 1
  print('test knowte', request)
  if id is None:
    ret = Knowte.objects.all()
  else:
    ret = Knowte.objects.get(id=id)
  return JsonResponse({
    'text': ret.text
  })