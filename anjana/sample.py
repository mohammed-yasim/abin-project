from django.shortcuts import render,redirect,HttpResponse
from console.models import test_api
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import re
def ubc(request,default=None):
    referer = request.META.get('HTTP_REFERER')
    print('Referer',referer)
    if not referer:
        print('here not')
        return default

    # remove the protocol and split the url at the slashes
    referer = re.sub('^https?:\/\/', '', referer).split('/')
    print(referer)
    if referer[0] != request.META.get('HTTP_HOST'):
        print('server not',request.META.get('HTTP_HOST'))
        return default

    # add the slash at the relative path's view and finished
    referer = u'/' + u'/'.join(referer[1:])
    print(referer)
    return referer
def checker_get(request):
    try:
        url = request.GET['next']
        return redirect(url)
    except:
        pass
def pass_check(requested,uri):
    try:
        data = requested.POST['next']
        url="%s?next=%s"%(uri,data)
        return url
    except :
        return uri
def del_auth(request):
    logout(request)
    return redirect('/official_admin/login')
def auth_form(request):
    try:
        a =  ubc(request)
        print('authform',  a)   
        if(a != '/official_admin/auth'):
            del request.session['officialloginerror']
    except:
        pass
    ubc(request)
    if request.user.is_authenticated:
        checker_get(request)
        return redirect('/official_admin/dashboard') 
    return render(request,'auth_base.html')
def auth_request(request):
    try:
        del request.session['officialloginerror']
    except:
        pass
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        try:
            url = request.POST['next']
            return redirect(url)
        except:
            return redirect('/official_admin/dashboard')
    else:
        request.session['officialloginerror'] = "Invalid Username or Password"
        return HttpResponse("There was an error with your E-Mail/Password combination. Please try again.<a href='%s'><script type='text/javascript'>window.location = '%s'</script>"%(pass_check(request,'/official_admin/login'),pass_check(request,'/official_admin/login'))) 
