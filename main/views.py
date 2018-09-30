from django.shortcuts import render
from django.http import JsonResponse
from main.models import Knowte

# Create your views here.


def knowte(request):
  ret = []
  id = 1
  print('test knowte', request)
  if id is None:
    objects = Knowte.objects.all()
    for obj in object:
      ret.append({
        'text': obj.text
      })
  else:
    obj = Knowte.objects.get(id=id)
    ret = [{
      'text': obj.text
    }]
  return JsonResponse({ 'objects': ret })