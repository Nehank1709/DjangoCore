from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import random

# Create your views here.
def index(request):
    lucky_number = random.randint(100,999)
    vegetables = ["Tomato 🍅", "Potato 🥔", "Cabbage 🥬", "Onion 🧅", "Cucumber 🥒"]

    person_age = 20

    for vegetable in vegetables:
        print(vegetable)

    cities = [
    {"name": "Mumbai", "population": 20411000, "country": "India"},
    {"name": "Delhi", "population": 31870000, "country": "India"},
    {"name": "New York", "population": 13707000, "country": "USA"},
    {"name": "Hyderabad", "population": 10918000, "country": "India"},
    {"name": "Tokyo", "population": 11009000, "country": "Japan"}
]

    context = {"lucky_number" : lucky_number, "vegetables": vegetables, "person_age": person_age, "cities":cities}
    print(lucky_number)
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def dynamic_url(request,id, name):
    print(f"This is the value received from end point {id}")
    return render(request, 'dynamic_url.html', context={'id':id, 'name':name})

# class HomeView(View):
#     template_name="index.html"

#     def get(self, request):
#         return render(request, self.template_name)
    
#     def post(self, request):
#         return render(request, self.template_name)
