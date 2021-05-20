from django.shortcuts import redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def login_submit(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
            return redirect('/PATH/')
    else:
         return redirect('/LOGIN-PAGE/?ERROR=0')
def logout(request):
    logout();
    return redirect('/LOGIN-PAGE/?ERROR=0')
    
@login_required
def home(request):
    return(HttpResponse("Hello"))
