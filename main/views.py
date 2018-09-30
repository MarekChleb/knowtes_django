from django.shortcuts import render
from main.models import Knowte

# Create your views here.


def knowte(request, id=None):
  ret = {}
  if id is None:
    ret = Knowte.objects.all()
  else:
    ret = Knowte.objects.get(id=id)
  return ret