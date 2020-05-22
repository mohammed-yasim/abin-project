from django.shortcuts import render, redirect, HttpResponse
from project_admin.models import Global_variable as gvar
from .models import official_athorities_list, official_user
from portal.models import Portal_user_profile, food_item,food_item_list_in_orders,foods_order,Test_Result,Medicine_list,Medicare_order
import hashlib,datetime
# Create your views here.


def index(request):
    if request.session.has_key('official'):
        return redirect('/portal_official/dashboard')
    else:
        return redirect('/portal_official/login')


def dashboard(request):
    if not request.session.has_key('official'):
        return redirect('/portal_official/login')
    return render(request, 'po_dashboard.html')
# -----------------------------------------
# @@@@@@@@@
# PROFILES
# @@@@@@@@@
# -----------------------------------------


def portal_users(request):
    if not request.session.has_key('official'):
        return redirect('/portal_official/login')
    currentlb = official_athorities_list.objects.get(
        localbody_name=request.session['localbody'], localbody_type=request.session['lbtype'])
    data = Portal_user_profile.objects.filter(localbody=currentlb)
    if data.count() == 0:
        data = None
    return render(request, 'po_portalusers.html', {'data': data})


def userprofile(request):
    html = """ <table class="table table-responsive table-bordered"> """
    login = request.GET['login']
    userdata = Portal_user_profile.objects.get(login=login)
    html += """  <tr><th class="col">Name</th><td class="col">%s %s</td></tr> """ % (
        userdata.fname, userdata.lname)
    html += """  <tr><th>Email</th><td>%s</td></tr> """ % (userdata.email)
    html += """  <tr><th>Phone Number</th><td>%s</td></tr> """ % (
        userdata.login)
    html += """  <tr><th>Alternate Number</th><td>%s</td></tr> """ % (
        userdata.altno)
    html += """  <tr><th>Address</th><td>%s</td></tr> """ % (userdata.address)
    html += """  <tr><th>Place</th><td>%s</td></tr> """ % (userdata.place)
    html += """  <tr><th>City</th><td>%s</td></tr> """ % (userdata.city)
    html += """  <tr><th>PIN code</th><td>%s</td></tr> """ % (userdata.pincode)
    html += """</table><script>$(document).ready(function(){$("#ProfileViewModalLabel").text("%s`s Profile");});</script>""" % (
        userdata.fname)
    return HttpResponse(html)
# -----------------------------------------
# @@@@@@@@@
# KITCHEN
# @@@@@@@@@
# -----------------------------------------


def kitchen(request):
    if not request.session.has_key('official'):
        return redirect('/portal_official/login')
    else:
        return render(request, 'po_kitchen.html')


def kitchen_orders(request):
    if not request.session.has_key('official'):
        return redirect('/portal_official/login')
    else:
        try:
            dated = request.GET['date'] 
        except:
            now = datetime.datetime.now()
            dated = now.strftime("%Y-%m-%d")
        try:
            currentlb = official_athorities_list.objects.get(localbody_name=request.session['localbody'], localbody_type=request.session['lbtype'])
            foodorderedlist = food_item_list_in_orders.objects.filter(localbody=currentlb,item_date = dated)
            qfoodorders = foods_order.objects.filter(localbody=currentlb,order_date = dated)
        except AssertionError:
            pass
        return render(request, 'po_kitchen_orders.html',{'data':qfoodorders,'list':foodorderedlist})


def kitchen_process(request):
    if not request.session.has_key('official'):
        return HttpResponse("""<script>window.location="/portal_official/login"</script>""")
    try:
        html = """  """
        if request.GET['items'] == 'all':
            try:
                dated = request.GET['date'] 
            except:
                now = datetime.datetime.now()
                dated = now.strftime("%Y-%m-%d")
            try:
                currentlb = official_athorities_list.objects.get(
                    localbody_name=request.session['localbody'], localbody_type=request.session['lbtype'])
                items = food_item.objects.filter(localbody=currentlb,item_date = dated)
                for item in items:
                    html += """
                    <div class="col-xl-3 col-md-6 mb-4">
            <div class="card border-left-primary shadow h-100 py-2">
                <div class="card-body">
                    <div class="row no-gutters align-items-center">
                        <div class="col mr-2">
                            <div class="text-xs font-weight-bold text-primary text-uppercase mb-1">%s</div>
                            <div class=" mb-0 text-gray-800">%s</div>
                            <div class="h6 mb-0 text-gray-500">Quantity : %s</div>
                             <div class="h6 mb-0 font-weight-bold text-gray-800">%s</div>
                        </div>
                        <div class="col-auto">
                            <i class="fas fa-hamburger fa-2x text-gray-300"></i>
                        </div>
                    </div>
                </div>
            </div>
        </div> """ %(item.item_name,item.item_description,item.item_qty,item.item_price)
            except:
                html += """ No Items Found """
            html += """ <div class="col-xl-1 col-md-2 mb-4">
            <div class=" h-100 py-2">
    
            <div class="row no-gutters align-items-center">
            <div class="col">
            <button onclick="addfooditem()" class="btn btn-white"><i class="fas fa-plus fa-2x text-primary-300"></i></button>
            </div>
            </div>
            </div>
            </div>"""
            return HttpResponse(html)
    except:
        pass
    try:
        html = """  """
        if request.GET['items'] == 'addnewitem':
            try:
                item_name = request.GET['itemname']
                item_description = request.GET['itemdescription']
                item_price = request.GET['itemprice']
                item_qty = request.GET['itemqty']
                currentlb = official_athorities_list.objects.get(
                    localbody_name=request.session['localbody'], localbody_type=request.session['lbtype'])
                item = food_item(
                    item_name=item_name,
                    item_description=item_description,
                    item_price=float(item_price),
                    item_qty=int(item_qty),
                    item_date= request.GET['item_date'],
                    localbody=currentlb
                    ).save()
                html+=""" Item '%s' Added  """ %(item_name)
            except:
                html+=""" Error """
            return HttpResponse(html)
    except AssertionError as error :
        return HttpResponse(0)

# -----------------------------------------
# @@@@@@@@@
# LOGIN
# @@@@@@@@@
# -----------------------------------------


def login(request):
    if request.session.has_key('official'):
        return redirect('/portal_official/dashboard')
    elif request.POST:
        if request.session.has_key('error') and request.POST['csrfmiddlewaretoken'] == request.session['error']:
            del request.session['error']
            return redirect('/portal_official/login')
        if request.session.has_key('status') and request.POST['csrfmiddlewaretoken'] == request.session['status']:
            del request.session['status']
            return redirect('/portal_official/login')
        try:
            email = request.POST['email']
            password = hashlib.md5(request.POST['user_passwd'].encode())
            password = password.hexdigest()
            print("init.................................")
            try:
                reg_login = official_user.objects.get(
                    email=email, passwd=password)
                localbody = official_athorities_list.objects.get(
                    localbody_admin=official_user.objects.get(email=email, passwd=password))
            except official_user.DoesNotExist:
                reg_login = None
                localbody = None
            print(reg_login)
            if reg_login:
                request.session['status'] = request.POST['csrfmiddlewaretoken']
                request.session['official'] = request.POST['email']
                request.session['official_name'] = reg_login.contact_person
                request.session['official_admin'] = reg_login.is_admin
                request.session['localbody'] = reg_login.localbody_name
                request.session['lbtype'] = localbody.localbody_type
                request.session['official_token'] = request.POST['csrfmiddlewaretoken']
                try:
                    del request.session['error']
                except:
                    pass
                return redirect('/portal_official/dashboard')
            else:
                raise Exception
        except:
            request.session['error'] = request.POST['csrfmiddlewaretoken']
            return render(request, 'po_login.html', {'error': 'Invalid Email or password'})
    else:
        return render(request, 'po_login.html')


def logout(request):
    try:
        del request.session['official']
        del request.session['official_name']
        del request.session['official_admin']
        del request.session['localbody']
        del request.session['lbtype']
        del request.session['official_token']
        del request.session['status']
    except:
        pass
    return redirect('/portal_official/')


def signup(request):
    if request.session.has_key('official'):
        return redirect('/portal_official/dashboard')
    elif request.POST:
        if request.session.has_key('error') and request.POST['csrfmiddlewaretoken'] == request.session['error']:
            del request.session['error']
            return redirect('/portal_official/signup')
        if request.session.has_key('status') and request.POST['csrfmiddlewaretoken'] == request.session['status']:
            del request.session['status']
            return redirect('/portal_official/signup')
        try:
            state = request.POST['user_state']
            district = request.POST['user_district']
            lbtype = request.POST['user_localbody']
            lbname = request.POST['user_localbody_name']
            email = request.POST['user_email']
            cpname = request.POST['user_person']
            contact = request.POST['user_contact']
            password = hashlib.md5(request.POST['user_password'].encode())
            confirm = hashlib.md5(request.POST['user_passwd'].encode())
            password = password.hexdigest()
            confirm = confirm.hexdigest()
            print(password, confirm)
            request.session['error'] = request.POST['csrfmiddlewaretoken']
            if(state == '' or district == '' or lbtype == '' or lbname == '' or email == '' or cpname == '' or contact == '' or password == '' or contact == ''):
                request.session['error'] = request.POST['csrfmiddlewaretoken']
                return render(request, 'po_signup.html', {'error': "Please fill all the required details!"})
                # return redirect('/portal_official/signup?e=Please fill all the required details!')
            elif (password != confirm):
                return render(request, 'po_signup.html', {'error': "Password Miss Match!"})
                # return redirect('/portal_official/signup?error=Password Miss Match!&user_localbody_name=%s&user_email=%s&user_person=%s&user_contact=%s'%(lbname,email,cpname,contact))
            elif(not state or not district):
                return render(request, 'po_signup.html', {'error': "Error in Proessed data"})
            else:
                try:
                    official_user.objects.get(email=email)
                    return render(request, 'po_signup.html', {'error': "Email Already Registered"})
                except:
                    pass
                try:
                    official_user.objects.get(contact_no=contact)
                    return render(request, 'po_signup.html', {'error': "Mobile Number Already Registered"})
                except:
                    pass
                try:
                    official_athorities_list.objects.get(
                        localbody_state=state, localbody_district=district, localbody_type=lbtype, localbody_name=lbname)
                    return render(request, 'po_signup.html', {'error': "LocalBody Already Registered"})
                except:
                    pass
                del request.session['error']
        except:
            return redirect('/portal_official/signup?e=Error! Unavailable at this moment')
        try:
            lbname = lbname.lower()
            user = official_user(
                email=email,
                passwd=confirm,
                designation='',
                contact_no=contact,
                contact_person=cpname,
                localbody_name=lbname,
            ).save()
            authority = official_athorities_list(
                localbody_state=state,
                localbody_district=district,
                localbody_type=lbtype,
                localbody_name=lbname,
                localbody_admin=official_user.objects.get(
                    email=email, passwd=confirm)
            ).save()
            request.session['status'] = request.POST['csrfmiddlewaretoken']
            result = """"
            <html><head><script>alert('Registration Successfull Please Login');
            window.location = '/portal_official/';</script></head></html>"""
            return HttpResponse(result)
        except:
            result = """"
            <html><head><script>alert('Registration Module : Error while Processing data');
            window.location = '/portal_official/signup';</script></head></html>"""
            return HttpResponse(result)
    else:
        return render(request, 'po_signup.html', {})


def testresult(request):
    if not request.session.has_key('official'):
        return redirect('/portal_official/login')
    else:
        try:
            dated = request.GET['date'] 
        except:
            now = datetime.datetime.now()
            dated = now.strftime("%Y-%m-%d")
        try:
            currentlb = official_athorities_list.objects.get(localbody_name=request.session['localbody'], localbody_type=request.session['lbtype'])
            testresults = Test_Result.objects.filter(localbody=currentlb)
        except AssertionError:
            pass
        return render(request, 'po_testresult.html',{'data':testresults})


def usertestresultprofile(request):
    html = """ <table class="table table-responsive table-bordered"> """
    login = request.GET['login']
    userdata = Portal_user_profile.objects.get(login=login)
    currentlb = official_athorities_list.objects.get(localbody_name=request.session['localbody'], localbody_type=request.session['lbtype'])
    testresults = Test_Result.objects.filter(localbody=currentlb,user_id=userdata)
    html += """  <tr><th class="col">Name</th><td class="col">%s %s</td></tr> """ % (
        userdata.fname, userdata.lname)
    html += """  <tr><th>Email</th><td>%s</td></tr> """ % (userdata.email)
    html += """  <tr><th>Phone Number</th><td>%s</td></tr> """ % (
        userdata.login)
    html += """  <tr><th>Alternate Number</th><td>%s</td></tr> """ % (
        userdata.altno)
    html += """  <tr><th>Address</th><td>%s</td></tr> """ % (userdata.address)
    html += """  <tr><th>Place</th><td>%s</td></tr> """ % (userdata.place)
    html += """  <tr><th>City</th><td>%s</td></tr> """ % (userdata.city)
    html += """  <tr><th>PIN code</th><td>%s</td></tr> """ % (userdata.pincode)

    html += """</table><script>$(document).ready(function(){$("#ProfileViewModalLabel").text("%s`s Profile");});</script>""" % (
        userdata.fname)
    html += """ <table class="table table-bordered"> <tr><th>Date</th><th>Body Temperature</th><th>Probability(%)</th></tr>""" 
    for data in testresults:
        html += """ <tr><td>%s</td><td>%s</td><td>%s</td></tr>""" % (data.test_date,data.fever,data.result)
    html += """ </table>""" 
    return HttpResponse(html)


# -----------------------------------------
# @@@@@@@@@
# MEDICINE
# @@@@@@@@@
# -----------------------------------------


def medicine(request):
    if not request.session.has_key('official'):
        return redirect('/portal_official/login')
    else:
        currentlb = official_athorities_list.objects.get(localbody_name=request.session['localbody'], localbody_type=request.session['lbtype'])
        med = Medicine_list.objects.filter(localbody = currentlb,deleted = False)

        return render(request, 'po_medicine.html',{'medicines':med})


def addmedicine(request):
    if not request.session.has_key('official'):
        return redirect('/portal_official/login')
    else:
        html = False 
        if request.POST:

            if request.session.get('medicine_crsftoken') != request.POST['csrfmiddlewaretoken']:
                try:
                    currentlb = official_athorities_list.objects.get(localbody_name=request.session['localbody'], localbody_type=request.session['lbtype'])
                    medicine_name = request.POST['medicine_name']
                    medicine_price = request.POST['medicine_price']
                    medicine_qty = request.POST['medicine_qty']
                    quantity_type = request.POST['quantity_type']

                    Medicine_list(
                        medicine_name=medicine_name,
                        medicine_price=float(medicine_price),
                        medicine_qty=int(medicine_qty),
                        quantity_type=quantity_type,
                        localbody=currentlb
                    ).save()
                    request.session['medicine_crsftoken']=request.POST['csrfmiddlewaretoken']
                    html = """ <div class="alert alert-success">Medicine Added Successfully</div> """
                except:
                    html = """ <div class="alert alert-danger">Not successfull</div>"""
            else:
                html = """ <div class="alert alert-warning">Duplicate Token <a href="addmedicine">Reset</a></div> """
        else:
            try:
                del request.session['medicine_crsftoken']
            except:
                pass
        return render(request, 'po_addmedicine.html',{'status':html})

def medicine_deleted(request):
    try:
        currentlb = official_athorities_list.objects.get(localbody_name=request.session['localbody'], localbody_type=request.session['lbtype'])
        delfield = Medicine_list.objects.get(localbody =currentlb,medicine_id = request.GET['medicineid'])
        delfield.deleted=True
        delfield.save()
        html = """ <script> alert("Medicine Deleted"); window.location='/portal_official/medicine'; </script> """
        return HttpResponse(html)
    except:
       html = """ <script> alert("Error occured");window.location='/portal_official/medicine'; </script> """ 
       return HttpResponse(html) 

def med_save_update(request):
    try:
        currentlb = official_athorities_list.objects.get(localbody_name=request.session['localbody'], localbody_type=request.session['lbtype'])
        updatefield = Medicine_list.objects.get(localbody =currentlb,medicine_id = request.GET['medicineid'])
        updatefield.medicine_name = request.POST['medicine_name']
        updatefield.medicine_price = request.POST['medicine_price']
        updatefield.medicine_qty = request.POST['medicine_qty']
        updatefield.quantity_type = request.POST['quantity_type']
        updatefield.save()
        html = """ <script> alert("Medicine Updated"); window.location='/portal_official/medicine'; </script> """
        return HttpResponse(html)
    except:
       html = """ <script> alert("Error occured");window.location='/portal_official/medicine'; </script> """ 
       return HttpResponse(html)

def medicine_update(request):
    if not request.session.has_key('official'):
        return redirect('/portal_official/login')
    else:
        currentlb = official_athorities_list.objects.get(localbody_name=request.session['localbody'], localbody_type=request.session['lbtype'])
        med = Medicine_list.objects.get(localbody = currentlb,medicine_id = request.GET['medicineid'])

        return render(request, 'po_medicine_update.html',{'medicine':med})

def mediorders(request):
    if not request.session.has_key('official'):
        return redirect('/portal_official/login')
    else:
        currentlb = official_athorities_list.objects.get(localbody_name=request.session['localbody'], localbody_type=request.session['lbtype'])
        medorders = Medicare_order.objects.filter(localbody = currentlb)
        
        return render(request, 'po_mediorders.html',{'medorder':medorders})