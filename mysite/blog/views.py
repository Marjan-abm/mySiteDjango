from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse



my_data = {
    "Name":"Marjan",
    "Track":"Backend (Python)",
    "Message":"Hi Mentor, thank you for your support!"
}

# Create your views here.
def index(request):
    return JsonResponse(my_data)