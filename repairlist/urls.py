from django.urls import path
from .views import CreateRepairList,EditRepairList,AddVersion,BulkUpload


urlpatterns = [
    path('',CreateRepairList),
    path('<int:repair_id>',EditRepairList),
    path('add-version/',AddVersion),
    path('bulk-upload/', BulkUpload)
]