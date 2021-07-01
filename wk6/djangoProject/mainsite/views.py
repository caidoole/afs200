from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

def home (request):
    return render(request, 'mainsite/home.html')
    
def signup (request):
    return render(request, 'registration/signup.html')

class signup (generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'