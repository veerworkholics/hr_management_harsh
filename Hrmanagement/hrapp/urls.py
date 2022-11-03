from django.urls import path
from.import views

urlpatterns = [
   path("",views.signin,name="signin"),
   path("index",views.index,name="index"),
   path("profile",views.profile,name="profile"),
   path("login",views.signin,name="signin"),
   path("logout",views.logout,name="logout")
]
