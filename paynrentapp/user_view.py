from django.db import connection
from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from paynrentapp.serializers import AdministratorSerializer
from paynrentapp.models import Administrator
from . import tuple_to_dict
from django.http.response import JsonResponse
from paynrentapp.serializers import VehiclesSerializer
from paynrentapp.models import Vehicles
import json
import datetime


@api_view(['GET','POST','DELETE'])
def Index(request):
    return render(request,'Index.html')

@api_view(['GET','POST','DELETE'])
def DisplaySelectedVehicle(request):
    vehicle=request.GET['vehicle']
    selected_vehicle=json.loads(vehicle)
    print("xxxxxxxx",selected_vehicle)
    userdata=request.session["USERDATA"]

    st=datetime.datetime.strptime(userdata['starttime'],"%Y/%m/%d %H:%M")
    et=datetime.datetime.strptime(userdata['endtime'],"%Y/%m/%d %H:%M")
    userdata['starttime']=datetime.datetime.strftime(st,"%a,%d %b %Y")
    userdata['endtime']=datetime.datetime.strftime(et,"%a,%d %b %Y")
    d=userdata['days'].split(":")
    userdata['days']=d[0]+" Days"+" "+d[1]+" Hours"
    userdata['fare']=selected_vehicle['price']
    hr=int(selected_vehicle['price'])//24
    userdata['amount']=int(d[0])*int(selected_vehicle['price'])+(hr*int(d[1]))
    userdata['netamount']=userdata['amount']+400

    return render(request,'DisplaySelectedVehicle.html',{'vehicle':selected_vehicle,'userdata':userdata})

@api_view(['GET','POST','DELETE'])
def ShowVehicleList(request):
   userdata={'mobileno':'','city':request.GET['city'],'starttime':request.GET['starttime'],'endtime':request.GET['endtime'],'days':request.GET['dh']}
   request.session["USERDATA"]=userdata
   return JsonResponse(userdata,safe=False)

@api_view(['GET','POST','DELETE'])
def SetMobileAndEmail(request):
  
   userdata=request.session["USERDATA"]
   userdata['mobileno']=request.GET['mobileno']
   userdata['emailaddress']=request.GET['emailaddress']
   userdata['amount']=request.GET['amount']
   request.session["USERDATA"]=userdata

   return JsonResponse(userdata,safe=False)

@api_view(['GET','POST','DELETE'])
def UserVehicleList(request):
    userdata=request.session["USERDATA"]
    print("uuussssseerrr",userdata)
    return render(request,'UserVehicleList.html',{'userdata':userdata})

@api_view(['GET','POST','DELETE'])
def VehicleDisplayForUser(request):
    try:
        if request.method == 'GET':
            if(request.GET['param']=="all"):
             q = "select V.*,(select C.categoryname from paynrentapp_category C where C.id=V.categoryid) as categoryname, (select S.subcategoryname from paynrentapp_subcategory S where S.id=V.subcategoryid) as subcategoryname,(select S.companyname from paynrentapp_subcategory S where S.id=V.subcategoryid) as companyname from paynrentapp_vehicles V"
            else:
             q = "select V.*,(select C.categoryname from paynrentapp_category C where C.id=V.categoryid) as categoryname, (select S.subcategoryname from paynrentapp_subcategory S where S.id=V.subcategoryid) as subcategoryname,(select S.companyname from paynrentapp_subcategory S where S.id=V.subcategoryid) as companyname from paynrentapp_vehicles V where V.subcategoryid in (select id from paynrentapp_subcategory where companyname in({}))".format(request.GET['param'])
            print(q)
            cursor = connection.cursor()
            cursor.execute(q)
            records = tuple_to_dict.ParseDictMultipleRecord(cursor)
            print("xxxxxxxxxx",records)
            return JsonResponse(records,safe=False)
    except Exception as e:
        print("Error : " ,e)
        return JsonResponse(records,safe=False)