from django.urls import path
from.import views

urlpatterns = [
   path("",views.signin,name="signin"),
   path("index",views.index,name="index"),
   path("profile",views.profile,name="profile"),
   path("profileUpdate",views.profileUpdate,name="profileUpdate"),
   path("login",views.signin,name="signin"),
   path("logout",views.logout,name="logout"),
   path("updateimage",views.updateimage,name="updateimage"),
   path('roleapi/',views.role_api)
]
