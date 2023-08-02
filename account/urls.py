from django.urls import path
from .views import Register, Login, UserView, Logout, ChangePassword

urlpatterns = [
    path("register/", Register),
    path("login/", Login),
    path("", UserView),
    path("logout/", Logout),
    path("change-password/", ChangePassword),
]
