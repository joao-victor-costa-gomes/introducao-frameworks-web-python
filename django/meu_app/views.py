from django.shortcuts import render
from .models import Usuario

def hello(request):

    usuarios = Usuario.objects.all()

    return render(request, 'index.html', {'usuarios':usuarios})
