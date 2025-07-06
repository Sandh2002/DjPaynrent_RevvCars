from rest_framework import serializers 
from paynrentapp.models import  Category
from paynrentapp.models import  SubCategory
from paynrentapp.models import  Vehicles
from paynrentapp.models import  Administrator
class CategorySerializer(serializers.ModelSerializer):
        class Meta:
          model = Category
          fields = ('id', 'categoryname','description','icon')
class SubCategorySerializer(serializers.ModelSerializer):
        class Meta:
          model = SubCategory
          fields = ('id','categoryid','companyname', 'subcategoryname','description','icon')     
class VehiclesSerializer(serializers.ModelSerializer):
        class Meta:
          model = Vehicles
          fields = ('id', 'categoryid', 'subcategoryid', 'modelyear', 'variant', 'price', 'insured', 'registrationno', 'ownername', 'mobileno', 'color', 'fueltype', 'noofseats', 'transmissiontype', 'picture')          
class AdministratorSerializer(serializers.ModelSerializer):
        class Meta:
          model = Administrator
          fields = ('id', 'adminname','mobileno','emailid','password')



