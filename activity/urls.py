from django.urls import path
from .views import CreateComment,Comment,CreateActivity,EditStatus,EditDate,AddQuoteRepair, GetActivity

urlpatterns = [
    path('create-comment/', CreateComment),
    path('comment/<int:container_id>', Comment),
    path('create-activity/<int:container_id>', CreateActivity),
    path('status/<int:activity_id>', EditStatus),
    path('date/<int:activity_id>', EditDate),
    path('<int:activity_id>/attach-repair/', AddQuoteRepair),
    path('<int:container_id>',GetActivity),
]