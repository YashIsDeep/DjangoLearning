from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(project):
	return HttpResponse("<h1>A new world is coming.</h1>")