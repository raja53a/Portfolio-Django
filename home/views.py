from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request): 
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        content =request.POST['content']
        contact=Contact(name=name, email=email, content=content)
        contact.save()
        
    return render(request,'home/index.html')