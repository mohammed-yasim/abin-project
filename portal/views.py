from django.shortcuts import render,HttpResponse,redirect
from .models import Portal_user,Portal_user_profile,food_item,foods_order,food_item_list_in_orders,Test_Result
from portal_official.models import official_athorities_list
from random import randint
from datetime import datetime,timedelta
from plyer import notification
import uuid
#------------------------------------------------------------
#************************************************************
#------------------------------------------------------------

#------------------------------------------------------------
#************************************************************
#------------------------------------------------------------

# Create your views here.
def index(request):
    if request.session.has_key('login'):
        return redirect('/portal/dashboard')
    else:
        return render(request,'portal_home.html')
def dashboard(request):
    if not request.session.has_key('login'):
        return redirect('/portal/auth')
    else:
        try:
            login = request.session['login']
            profile = Portal_user_profile.objects.get(login=login)
        except (Portal_user_profile.DoesNotExist):
            return redirect('/portal/q/profile')
        return render(request,'portal/dashboard.html')
#------------------------------------
def profile_save(request):
    if not request.session.has_key('login'):
        return redirect('/portal/auth')
    if request.POST:
        try:
            login = request.session['login']
            profile_status= request.POST['profile_status']
            if profile_status == '0':
                state = request.POST['state']
                district = request.POST['district']
                lbname = request.POST['lbname']
                lbtype = request.POST['lbtype']
                if(state != 'other' or district != 'other' or lbname != 'other'):
                    localbody = official_athorities_list.objects.get(localbody_state = state, localbody_district= district, localbody_name=lbname, localbody_type=lbtype)
                else:
                    localbody = None
                user= Portal_user.objects.get(
                    login = login
                )
                profile_data = Portal_user_profile.objects.create(
                    login = user,
                    localbody = localbody,
                    fname = request.POST['fname'],
                    lname = request.POST['lname'],
                    email = request.POST['email'],
                    altno = request.POST['altno'],
                    address = request.POST['address'],
                    place = request.POST['place'],
                    city = request.POST['city'],
                    pincode = request.POST['pincode']
                )
                profile_data.save()
                result = """<script>alert('profile updated');window.location = '/portal/dashboard';</script>"""
                return HttpResponse(result)
            elif profile_status == '1':
                state = request.POST['state']
                district = request.POST['district']
                lbname = request.POST['lbname']
                lbtype = request.POST['lbtype']
                if(state != 'other' or district != 'other' or lbname != 'other'):
                    localbody = official_athorities_list.objects.get(localbody_state = state, localbody_district= district, localbody_name=lbname, localbody_type=lbtype)
                else:
                    localbody = None
                user= Portal_user.objects.get(
                    login = login
                )
                profile_data = Portal_user_profile.objects.get(login=user)
                profile_data.localbody = localbody
                profile_data.fname = request.POST['fname']
                profile_data.lname = request.POST['lname']
                profile_data.email = request.POST['email']
                profile_data.altno = request.POST['altno']
                profile_data.address = request.POST['address']
                profile_data.place = request.POST['place']
                profile_data.city = request.POST['city']
                profile_data.pincode = request.POST['pincode']
                profile_data.save()
                result = """<script>alert('profile Edit updated');window.location = '/portal/q/profile';</script>"""
                return HttpResponse(result)
            else:
                result = """<script>alert('Key Not Set');window.location = '/portal/q/profile';</script>"""
                return HttpResponse(result)
        except AssertionError as error:
            return HttpResponse(error)
    else:
        return redirect('/portal/q/profile')

#-------------------------------------
def queries(request,query='profile'):
    if not request.session.has_key('login'):
        return redirect('/portal/auth')
    else:
        if query == 'profile':
            profile_user = None
            try:
                login = request.session['login']
                profile = Portal_user_profile.objects.get(login=login)
                profile_status = "1"
                profile_user = dict()
                profile_user['state'] = profile.localbody.localbody_state
                profile_user['district'] = profile.localbody.localbody_district
                profile_user['lbname'] = profile.localbody.localbody_name
                profile_user['lbtype'] = profile.localbody.localbody_type

                profile_user['fname'] = profile.fname
                profile_user['lname'] = profile.lname
                profile_user['email'] = profile.email
                profile_user['altno'] = profile.altno
                profile_user['address'] = profile.address
                profile_user['place'] = profile.place
                profile_user['city'] = profile.city
                profile_user['pincode'] = profile.pincode

        
                print(profile.localbody.localbody_state)
            except (Portal_user_profile.DoesNotExist):
                profile_status = "0"
            return render(request,'portal/profile.html',{'profile_status':profile_status,'profile':profile_user})
        else:
            try:
                login = request.session['login']
                profile = Portal_user_profile.objects.get(login=login)
            except (Portal_user_profile.DoesNotExist):
                return redirect('/portal/q/profile')
            #------------------------------------------------------------
            #************************************************************
            #------------------------------------------------------------
            if query == 'kitchen':
                try:
                    login = request.session['login']
                    currentlb = Portal_user_profile.objects.get(login = login)
                    now = datetime.now()
                    f_items = food_item.objects.filter(localbody = currentlb.localbody,item_date = now.strftime("%Y-%m-%d"))
                    foodorderedlist = food_item_list_in_orders.objects.filter(user=login)
                    qfoodorders = foods_order.objects.filter(user_id=currentlb,order_date = now.strftime("%Y-%m-%d"))
                    message = "<strong>No Item Found in %s %s Kitchen </strong> <br> Conatct Authority : %s - %s "%(currentlb.localbody.localbody_name,currentlb.localbody.localbody_type,currentlb.localbody.localbody_admin.contact_person,currentlb.localbody.localbody_admin.contact_no)
                    if f_items.count() == 0:
                        f_items = None
                    if qfoodorders.count() >= 3:
                        f_items = None
                        message = "Maxmum Limit (3)"
                    if qfoodorders.count() == 0:
                        qfoodorders = None
                    if foodorderedlist.count() == 0:
                        foodorderedlist = None
                except AssertionError:
                    f_items = None
                    qfoodorders = None
                    foodorderedlist = None
                    message = "An Error Occured"
                return render(request,'portal/kitchen.html',{'message':message,'food_items':f_items,'data':qfoodorders,'list':foodorderedlist})
            elif query == 'orderfood':
                try:
                    login = request.session['login']
                    currentlb = Portal_user_profile.objects.get(login = login)
                    now = datetime.now()
                    orders = {}
                    Total_price = 0.00
                    j = 1
                    j = 1
                    temp_data_food = ''
                    for key,value in request.POST.items():
                        if key.find('_id') != -1:
                            orders['order_%s'%(j)] = {'food_id':value}
                        if key.find('_qty') != -1:
                            if value != '0':
                                try:
                                    temp_data_food =  food_item.objects.get(item_id=orders['order_%s'%(j)]['food_id'])
                                except:
                                    pass
                                orders['order_%s'%(j)]['properties'] = temp_data_food
                                orders['order_%s'%(j)]['food_qty'] = value
                                Total_price += float(temp_data_food.item_price)*float(value)
                            if value == '0':
                                orders.pop('order_%s'%(j))
                                j-=1
                            j+=1
                    if Total_price == 0.00:
                        orders = None
                except AssertionError :
                    pass
                return render(request, 'portal/ajax_foodorder.html',{'orders':orders,"total":Total_price,'details':currentlb}) 
            elif query == 'confirmorder':
                try:
                    login = request.session['login']
                    currentlb = Portal_user_profile.objects.get(login = login)
                    now = datetime.now()
                    orders = ""
                    u_id = uuid.uuid4()
                    Total_price = 0.00
                    foodorders = foods_order(
                        order_date = now.strftime("%Y-%m-%d"),
                        total_price = float(request.POST['price']),
                        user_id = currentlb,
                        localbody = currentlb.localbody,
                        uid = u_id)
                    foodorders.save()
                    for key,value in request.POST.items():
                        print("Key:%s - value : %s"%(key,value))
                        if key.find('@id') != -1:
                            orders = value
                            print(orders)
                        if key.find('@qty') != -1:
                            print(value)
                            a = food_item_list_in_orders(
                                item_id = food_item.objects.get(item_id = orders),
                                item_qty = int(value),
                                item_date = now.strftime("%Y-%m-%d"),
                                uid = u_id,
                                user=login,
                                localbody= currentlb.localbody,
                            ).save()
                            print("loop1",a)
                        
                    foodorderedlist = food_item_list_in_orders.objects.filter(uid=u_id,user=login)
                    print("foodorderedlist",foodorderedlist)
                    #for data in foodorderedlist:
                    #    qfoodorders = foods_order.objects.get(uid=u_id)
                    #    print("Dataa",data)
                    #    qfoodorders.items_ordered.add(data)
                    #    qfoodorders.save()
                except AssertionError :
                    pass
                return  HttpResponse("<script>alert('Order Sucess'); window.location = '/portal/q/kitchen';</script>") 
            elif query == 'test':
                return render(request,'portal/test.html')
            elif query == 'gettestresult':
                if request.POST:
                    try:
                        login = request.session['login']
                        current_user = Portal_user_profile.objects.get(login = login)
                        now = datetime.now()

                        travel = int(request.POST['travel'])
                        fever = int(request.POST['fever'])
                        age = int(request.POST['age'])
                        pain = int(request.POST['pain'])
                        nose = int(request.POST['nose'])
                        breath = int(request.POST['breath'])
                        other = int(request.POST['other'])

                        import pickle
                        file = open('model.pkl', 'rb')
                        model = pickle.load(file)
                        file.close()
                        test_result=model.predict_proba([[fever,pain,age,nose,breath,breath,other]])
                        result = float(test_result[0][1])*100
                        result = round(result,2)
                        Test_Result(user_id = current_user,
                        localbody = current_user.localbody,
                        test_date = now.strftime("%Y-%m-%d"),
                        fever = fever,
                        age = age,
                        pain = pain,
                        nose = nose,
                        breath = breath,
                        travel = travel,
                        other = other,
                        disease = request.POST['disease'],
                        result = result
                         ).save()
                        

                    except AssertionError as Error:
                        return HttpResponse(Error)
                else:
                    return HttpResponse("Errir in PoSt")
                return render(request,'portal/gettestresult.html',{'result':result})
            else:
                return render(request,'portal/404.html')
            #------------------------------------------------------------
            #************************************************************
            #------------------------------------------------------------
def auth(request):
    if request.session.has_key('login'):
        return redirect('/portal')
    if request.method == 'POST' and 'login' in  request.POST:
        login = request.POST['login']
        try:
            login_object = Portal_user.objects.get(login=login)
            now = datetime.now()
            ex = datetime.strptime(str(login_object.otp_generated),"%Y-%m-%d %H:%M:%S")
            if (now-ex) > timedelta(minutes=5):
                login_object.otp = randint(11111,99999)
                login_object.otp_generated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                login_object.save()
        except:
            Portal_user.objects.create(login=login,otp=randint(11111,99999),otp_generated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")).save()
            login_object = Portal_user.objects.get(login=login)
        db_otp = str(login_object.otp)
        try:
            notification.notify(app_name='PY_SERVER',title='PY_SERVER',message=r'OTP is %s valid for 5 mins'%(db_otp),app_icon=None,timeout=15)
        except:
            print(db_otp)
        return render(request,'auth_otp.html',{"login":login})
    elif request.method == 'POST' and request.POST['mobile'] and request.POST['otp']:
        error_template = """ Invalid OTP """
        otp = str(request.POST['otp'])
        login =  str(request.POST['mobile'])
        login_object = Portal_user.objects.get(login=login)
        db_otp = str(login_object.otp)
        if db_otp==otp:
            request.session['login'] = login
            return redirect('/portal')
        else:
            try:
                notification.notify(app_name='PY_SERVER',title='PY_SERVER',message=r'OTP is %s valid for 5 mins'%(db_otp),app_icon=None,timeout=15)
            except:
                print(db_otp)
            return render(request,'auth_otp.html',{"login":login,'error':error_template})
    else:
        return render(request,'auth_login.html')
def logout(request):
    try:
        del request.session['login']
    except:
        pass
    return redirect('/portal/')