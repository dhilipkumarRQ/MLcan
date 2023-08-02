from django.urls import path
from .views import CreateComment,Comment

urlpatterns = [
    path('create-comment/', CreateComment),
    path('get-comment/', Comment)
]