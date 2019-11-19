from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, 'main/home.html')

def portfolio(request):
    return render(request, 'main/portfolio.html')

def cv(request):
    return render(request, 'main/cv.html')
    
def contact(request):
    return render(request, 'main/contact.html')

# Create your views here.
