from django.http import HttpResponse
from django.shortcuts import render


def index(request):
	return render(request, 'alumini/index.html')

def index1(request):
	return render(request, 'alumini/index1.html')	

def index2(request):
	return render(request, 'alumini/index2.html')		