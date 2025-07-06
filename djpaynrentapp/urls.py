"""djpaynrentapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from paynrentapp import category_view
from paynrentapp import subcategory_view
from paynrentapp import vehicles_view
from paynrentapp import admin_login
from paynrentapp import user_view


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/categoryinterface/',category_view.CategoryInterface),
    re_path(r'^api/categorysubmit',category_view.CategorySubmit),
    re_path(r'^api/displaycategory',category_view.DisplayCategory),
    re_path(r'^api/displaybycategoryid',category_view.DisplayByCategoryId),
    re_path(r'^api/editcategory/$',category_view.EditCategory),
    re_path(r'^api/displaybycategoryicon/$',category_view.DisplayByCategoryIcon),
    re_path(r'^api/save_category_icon',category_view.SaveCategoryIcon),
    re_path(r'^api/json_displaycategory',category_view.DisplayCategoryJSON),
    re_path(r'^api/subcategoryinterface/',subcategory_view.SubCategoryInterface),
    re_path(r'^api/subcategorysubmit',subcategory_view.SubCategorySubmit),
    re_path(r'^api/displaysubcategory',subcategory_view.DisplaySubCategory),
    re_path(r'^api/displaybysubcategoryid',subcategory_view.DisplayBySubCategoryId),
    re_path(r'^api/editsubcategory/$',subcategory_view.EditSubCategory),
    re_path(r'^api/displaybysubcategoryicon/$',subcategory_view.DisplayBySubCategoryIcon),
    re_path(r'^api/save_subcategory_icon',subcategory_view.SaveSubCategoryIcon),
    re_path(r'^api/display_json_subcategory',subcategory_view.DisplayBySubCategoryJSON),
    re_path(r'^api/vehiclesinterface/',vehicles_view.VehiclesInterface),
    re_path(r'^api/vehiclessubmit',vehicles_view.VehiclesSubmit),
    re_path(r'^api/displayvehicles',vehicles_view.DisplayVehicles),
    re_path(r'^api/displaybyvehiclesid',vehicles_view.DisplayByVehiclesId),
    re_path(r'^api/editvehicles/$',vehicles_view.EditVehicles),
    re_path(r'^api/displaybyvehiclesicon/$',vehicles_view.DisplayByVehiclesIcon),
    re_path(r'^api/save_vehicles_icon',vehicles_view.SaveVehiclesIcon),


    re_path(r'^api/adminlogin/',admin_login.AdminLogin),
    re_path(r'^api/checkadminlogin/',admin_login.CheckAdminLogin),
    
     re_path(r'^api/index/',user_view.Index),
     re_path(r'^api/uservehiclelist/',user_view.UserVehicleList),
     re_path(r'^api/userdisplayvehicles/',user_view.VehicleDisplayForUser),
     re_path(r'^api/displayselectedvehicle',user_view.DisplaySelectedVehicle), 
     re_path(r'^api/displayselectedvehicle/',user_view.DisplaySelectedVehicle),
     re_path(r'^api/showvehiclelist/',user_view.ShowVehicleList),
     re_path(r'^api/setemailmobile/',user_view.SetMobileAndEmail),

     re_path(r'^api/healthlogin/',admin_login.HealthLogin),
      re_path(r'^api/appplogin/',admin_login.apppLogin),
       re_path(r'^api/displayappp/',admin_login.displayappp
       ),
      

     

]
