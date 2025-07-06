from django.db import connection
from django.shortcuts import render
from django.http.response import JsonResponse
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from paynrentapp.serializers import SubCategorySerializer
from paynrentapp.models import SubCategory
from . import tuple_to_dict
from django.views.decorators.clickjacking import xframe_options_exempt

# Create your views here.
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def SubCategoryInterface(request):
    return render(request,'SubCategoryInterface.html')
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def SubCategorySubmit(request):
    if request.method=='POST':
        subcategory_serializer=SubCategorySerializer(data=request.data)
        if subcategory_serializer.is_valid():
            subcategory_serializer.save()
            return render(request,"SubCategoryInterface.html",{"message":"Record Submitted Successfully"})
        return render(request,"SubCategoryInterface.html",{"message":"Fail to Submit Record"})
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def DisplaySubCategory(request):
    try:
        if request.method == 'GET':
            q = "select S.*,(select C.categoryname from paynrentapp_category C where C.id=S.categoryid) as categoryname from paynrentapp_subcategory S"
            print(q)
            cursor = connection.cursor()
            cursor.execute(q)
            records = tuple_to_dict.ParseDictMultipleRecord(cursor)
            print("xxxxxxxxxx",records)
            

            return render(request,"SubCategoryDisplay.html",{'data':records})
    except Exception as e:
        print("Error",e)
        return render(request,"SubCategoryDisplay.html",{'data':{}}) 
    
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def DisplayBySubCategoryId(request):
   try: 
    if request.method=='GET':
     q = "select S.*,(select C.categoryname from paynrentapp_category C where C.id=S.categoryid) as categoryname from paynrentapp_subcategory S where S.id={0}".format(request.GET['id'])
     cursor=connection.cursor()
     cursor.execute(q)
     record=tuple_to_dict.ParseDictSingleRecord(cursor)
     return render(request,'DisplayBySubCategoryId.html',{'data':record})
   except Exception as e: 
       print(e)
       return render(request,'DisplayBySubCategoryId.html',{'data':{}})      
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def EditSubCategory(request): 
   try:
      if request.method=='GET':
         if (request.GET['btn']=="EDIT"):
          subcategory=SubCategory.objects.get(pk=request.GET['id'])
          subcategory.categoryid=request.GET['categoryid']
          subcategory.companyname=request.GET['companyname']
          subcategory.subcategoryname=request.GET['subcategoryname']
          subcategory.description=request.GET['description']
          subcategory.save()
         else:
            subcategory=SubCategory.objects.get(pk=request.GET['id'])  
            subcategory.delete()
         return redirect('/api/displaysubcategory')
   except Exception as e:  
      print("Error",e)
      return redirect('/api/displaysubcategory')     
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])  
def DisplayBySubCategoryIcon(request): 
   try:
      if request.method=='GET':   
        return render(request,'DisplaySubCategoryIcon.html',{'data':dict(request.GET)}) 
   except Exception as e:  
      print("Error",e)
      return render(request,'DisplaySubCategoryIcon.html',{'data':{}})    
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])  
def SaveSubCategoryIcon(request): 
   try:
      if request.method=='POST':
         subcategory=SubCategory.objects.get(pk=request.POST['id'])
         subcategory.icon=request.FILES['icon']
         subcategory.save()
         return redirect('/api/displaysubcategory')
   except Exception as e:
      print("Error",e)
      return redirect('/api/displaysubcategory')
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def DisplayBySubCategoryJSON(request):
   try: 
    if request.method=='GET':
     q="select * from paynrentapp_subcategory where categoryid={0}".format(request.GET['cid'])
     cursor=connection.cursor()
     cursor.execute(q)
     record=tuple_to_dict.ParseDictMultipleRecord(cursor)
     return JsonResponse(record,safe=False)
   except Exception as e: 
       print(e)
       return JsonResponse([],safe=False)