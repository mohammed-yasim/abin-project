from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.core import serializers
from .models import Global_variable
from portal_official.models import official_athorities_list
import json

# Create your views here.
def api(requests, query=''):
    json_template = {'response': 1,'status': 'success'}
    try:
        try:
            key = requests.GET['key']
            print("key",key)
            queryset = Global_variable.objects.filter(var_name = query,var_key = key).order_by('var_data')
        except:
            queryset = Global_variable.objects.filter(var_name = query,key="*").order_by('var_data')
        if(queryset.count() >= 1):
            post_liste = serializers.serialize('json', queryset)
            var_list = []
            for data in json.loads(post_liste):
                var_list.append(data['fields']['var_data'])
            json_template['data'] = var_list
            return HttpResponse(json.dumps(json_template), content_type="text/json-comment-filtered")
        else:
            json_template['response'] =  0
            json_template['status'] =  'error'
            json_template['message'] = "No data found"
            return JsonResponse(json_template)
    except:
        json_template['response'] =  0
        json_template['status'] =  'error'
        return JsonResponse(json_template)
def profile_api(requests,query=''):
    json_template = {'response': 1,'status': 'success'}
    try:
        if query == 'state':
            var_list = []
            try:
                queryset = official_athorities_list.objects.all()
            except:
                pass
            if(queryset.count() >= 1):
                post_liste = serializers.serialize('json', queryset)
                for data in json.loads(post_liste):
                    var_list.append(data['fields']['localbody_state'])
            var_list.append("Other")
            json_template['data'] = var_list
            return HttpResponse(json.dumps(json_template), content_type="text/json-comment-filtered")
        elif query == 'district':
            var_list = []
            try:
                key = requests.GET['key']
                queryset = official_athorities_list.objects.filter(localbody_state=key)
            except:
                pass
            if(queryset.count() >= 1):
                post_liste = serializers.serialize('json', queryset)
                for data in json.loads(post_liste):
                    var_list.append(data['fields']['localbody_district'])
            var_list.append("Other")
            json_template['data'] = var_list
            return HttpResponse(json.dumps(json_template), content_type="text/json-comment-filtered")
        elif query == 'localbody':
            var_list = []
            try:
                key = requests.GET['key']
                queryset = official_athorities_list.objects.filter(localbody_district=key)
            except:
                pass
            if(queryset.count() >= 1):
                post_liste = serializers.serialize('json', queryset)
                for data in json.loads(post_liste):
                    var_list.append("%s %s"%(data['fields']['localbody_name'],data['fields']['localbody_type'],))
            var_list.append("Other")
            json_template['data'] = var_list
            return HttpResponse(json.dumps(json_template), content_type="text/json-comment-filtered")
        elif query == 'localbody2':
            try:
                get_key = requests.GET['key']
                querywords = get_key.split()
                key = querywords[0].lower()
                print(key)
                queryset = official_athorities_list.objects.get(localbody_name=key)
                var_list1 = queryset.localbody_name
                var_list2 = queryset.localbody_type
            except:
                var_list1 = 'other'
                var_list2 = 'other'
            json_template['data1'] = var_list1
            json_template['data2'] = var_list2
            return HttpResponse(json.dumps(json_template), content_type="text/json-comment-filtered")
        else:
            json_template['response'] =  0
            json_template['status'] =  'error'
            json_template['message'] = "Query Not Set"
            return JsonResponse(json_template)


    except AssertionError as error:
        json_template['response'] =  0
        json_template['status'] =  'error'
        json_template['message'] = error
        return JsonResponse(json_template)