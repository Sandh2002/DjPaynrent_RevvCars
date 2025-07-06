from django.db import connection
from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from paynrentapp.serializers import VehiclesSerializer
from paynrentapp.models import Vehicles
from . import tuple_to_dict
from django.views.decorators.clickjacking import xframe_options_exempt
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def VehiclesInterface(request):
    return render(request,'VehiclesInterface.html')
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def VehiclesSubmit(request):
    if request.method=='POST':
        vehicles_serializer=VehiclesSerializer(data=request.data)
        if vehicles_serializer.is_valid():
            vehicles_serializer.save()
            return render(request,"VehiclesInterface.html",{"message":"Record Submitted Successfully"})
        return render(request,"VehiclesInterface.html",{"message":"Fail to Submit Record"})
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def DisplayVehicles(request):
   try: 
    if request.method=='GET':
       q = "select V.*,(select C.categoryname from paynrentapp_category C where C.id=V.categoryid) as categoryname, (select S.subcategoryname from paynrentapp_subcategory S where S.id=V.subcategoryid) as subcategoryname from paynrentapp_vehicles V"
       print(q)
       cursor=connection.cursor()
       cursor.execute(q)
       record=tuple_to_dict.ParseDictMultipleRecord(cursor)
       print("aaaaa",record)
       return render(request,'VehiclesDisplay.html',{'data':record})
   except Exception as e: 
       print(e)
       return render(request,'VehiclesDisplay.html',{'data':{}})      
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def DisplayByVehiclesId(request):
   try: 
    if request.method=='GET':
     q = "select V.*,(select C.categoryname from paynrentapp_category C where C.id=V.categoryid) as categoryname, (select S.subcategoryname from paynrentapp_subcategory S where S.id=V.subcategoryid) as subcategoryname from paynrentapp_vehicles V where V.id={0}".format(request.GET['id'])
     print(q)
     cursor=connection.cursor()
     cursor.execute(q)
     record=tuple_to_dict.ParseDictSingleRecord(cursor)
     return render(request,'DisplayByVehiclesId.html',{'data':record})
   except Exception as e: 
       print(e)
       return render(request,'DisplayByVehiclesId.html',{'data':{}})     
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def EditVehicles(request): 
   try:
      if request.method=='GET':
         if (request.GET['btn']=="EDIT"):
          vehicles=Vehicles.objects.get(pk=request.GET['id'])
          vehicles.categoryid=request.GET['categoryid']
          vehicles.subcategoryid=request.GET['subcategoryid']
          vehicles.modelyear=request.GET['modelyear']
          vehicles.variant=request.GET['variant']
          vehicles.price=request.GET['price']
          vehicles.insured=request.GET['insured']
          vehicles.registrationno=request.GET['registrationno']
          vehicles.ownername=request.GET['ownername']
          vehicles.mobileno=request.GET['mobileno']
          vehicles.color=request.GET['color']
          vehicles.fueltype=request.GET['fueltype']
          vehicles.noofseats=request.GET['noofseats']
          vehicles.transmissiontype=request.GET['transmissiontype']
          vehicles.save()
         else:
            vehicles=Vehicles.objects.get(pk=request.GET['id'])  
            vehicles.delete()
         return redirect('/api/displayvehicles')
   except Exception as e:  
      print("Error",e)
      return redirect('/api/displayvehicles')     
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])  
def DisplayByVehiclesIcon(request): 
   try:
      if request.method=='GET':   
        return render(request,'DisplayVehiclesIcon.html',{'data':dict(request.GET)}) 
   except Exception as e:  
      print("Error",e)
      return render(request,'DisplayVehiclesIcon.html',{'data':{}})       
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])  
def SaveVehiclesIcon(request): 
   try:
      if request.method=='POST':
         vehicles=Vehicles.objects.get(pk=request.POST['id'])
         vehicles.picture=request.FILES['picture']
         vehicles.save()
         return redirect('/api/displayvehicles')
   except Exception as e:
      print("Error",e)
      return redirect('/api/displayvehicles')
       