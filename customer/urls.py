from django.urls import path
from .views import AddCustomer, GetAllCustomer,GetCustomer


urlpatterns = [
    path('', AddCustomer),
    path('get-all/', GetAllCustomer),
    path('<int:customer_id>', GetCustomer),
]

