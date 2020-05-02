from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'home_index.html')
def about(request):
    return render(request,'home_about.html')
