from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
from method import seach_data 
from modeltranslation.fields import NONE
import json
from django.template.defaultfilters import length
def map(request):
    list= seach_data.SeachData()
    #print(list)
    return render(request, 'map_1.html',{'addresslist':list})

def index(request):
    list= seach_data.SeachData()
    return render(request, 'index.html',{'addresslist':list})

def filter(request):
    if request.method == "POST" and request.is_ajax():
        list1=[]
        data = request.POST
        code = data['code']
        minLat=data['minLat']
        maxLat=data['maxLat']
        minLng=data['minLng']
        maxLng=data['maxLng']
        print(code,minLat,maxLat,minLng,maxLng)
        filterlist= seach_data.FilterData(code,minLat,maxLat,minLng,maxLng)
        #print(filterlist)
        response = JsonResponse({"status": 'ajax传输成功', 'list': filterlist})
        return response
