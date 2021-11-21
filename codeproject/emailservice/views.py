from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    send_mail('Subject', 'Hello World', 'cassignment67@gmail.com', ['joneskimaminiel@gmail.com'], fail_silently = False)
    html = "Email Sent"
    return HttpResponse(html)
