from django.urls import path

from .views import GetAddContiner,GetContainer


urlpatterns = [
    path('',GetAddContiner),
    path('<int:container_id>', GetContainer) #handles edit container
]