from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def dynamic_url(request,id, name):
    print(f"This is the value received from end point {id}")
    return render(request, 'dynamic_url.html', context={'id':id, 'name':name})

class HomeView(View):
    template_name="index.html"

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        return render(request, self.template_name)
