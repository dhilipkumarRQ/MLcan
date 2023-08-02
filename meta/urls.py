from django.urls import path
from .views import Get_Container_Type,Get_Account_Type,Get_City,Get_Container_Height,Get_Container_Length,Get_Container_Year,Get_Damage_Area,Get_Province,Get_Quantity,Get_Repair_Area,Get_Repair_Type,Get_Yard

urlpatterns = [
    path('container-type/', Get_Container_Type),
    path('account-type/', Get_Account_Type),
    path('city/', Get_City),
    path('container-height/', Get_Container_Height),
    path('container-length/', Get_Container_Length),
    path('container-manufacture-year/', Get_Container_Year),
    path('damage-area/', Get_Damage_Area),
    path('province/', Get_Province),
    path('quantity/', Get_Quantity),
    path('repair-area/', Get_Repair_Area),
    path('repair-type/', Get_Repair_Type),   
    path('yard/', Get_Yard)
]

