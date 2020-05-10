from django.shortcuts import render

# Create your views here.
def coronagetresult(request):
    if request.POST:
        try:
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
                      
        except AssertionError as Error:
            return HttpResponse(Error)
    else:
        return HttpResponse("Error in PoSt")
    return render(request,'covidopentestresult.html',{'result':result})
          
def corona(request):
    return render(request,'covidopentest.html')

