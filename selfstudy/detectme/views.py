
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
def index(request):
    return render(request, 'detectme/home_page.html')