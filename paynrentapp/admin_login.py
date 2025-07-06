from django.db import connection
from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from paynrentapp.serializers import AdministratorSerializer
from paynrentapp.models import Administrator
from . import tuple_to_dict
from django.views.decorators.clickjacking import xframe_options_exempt

@api_view(['GET','POST','DELETE'])
def AdminLogin(request):
    return render(request,'AdminLogin1.html',{'status':True})
@api_view(['GET','POST','DELETE'])
def CheckAdminLogin(request):
    try:
        if request.method == 'GET':
            q = "select * from  paynrentapp_administrator  where (mobileno='{0}' or emailid='{0}') and password='{1}'".format(request.GET['mobileno'],request.GET['password'])

            print(q)
            cursor = connection.cursor()
            cursor.execute(q)
            record = tuple_to_dict.ParseDictMultipleRecord(cursor)
            if(len(record)==0):
                status=False
                return render(request,"AdminLogin1.html",{'status':status})
            else:
               status=True     
            
               return render(request,"DashBoard.html",{'data':record[0],'status':status})
    except Exception as e:
        print("Error : ",e)
        return render(request,"DashBoard.html",{'data':[],'status':False})
@api_view(['GET','POST','DELETE'])
def HealthLogin(request):
    return render(request,'healthplus.html',{'status':True})   
@api_view(['GET','POST','DELETE'])
def apppLogin(request):
    return render(request,'appp.html',{'status':True})   
@api_view(['GET','POST','DELETE'])
def displayappp(request):
    return render(request,'displayappp.html',{'status':True})    
   