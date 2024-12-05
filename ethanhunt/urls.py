from . import views
from django.urls import path,include
from rest_framework import routers
router=routers.DefaultRouter()
router.register(r'UserProfiles',views.UserProfileViewSet)

urlpatterns=[
    # path("",views.home,name="home"),
    path("",include(router.urls)),
    path("api-auth/",include("rest_framework.urls",namespace='rest_framework')),
    path("home/",views.home,name="home"),
    path("login/",views.login,name="login"),
    path("logout/",views.logout,name="logout"),
    path("signup/",views.signup,name="signup"),
]