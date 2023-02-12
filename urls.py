from django.urls import path,include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'Phil',PhilRegisterViewSet)
router.register(r'Ngo',NgoRegisterViewSet)
# router = routers.DefaultRouter()
# router.register(r'reg',getRegisterViewset)

urlpatterns = [
    path('register/', include(router.urls)),
    path('getfav/',favNgo.as_view()),
    path('home/',home),
    path('philLogin/',philLogin),
    path('ngoLogin/',ngoLogin),
    path('checkData/',checkData.as_view()),
    path('ngoDetails/',ngoDetailsViewSet.as_view()),
    path('searchNgos/',SearchedNgo.as_view()),
    path('prof/',UserViewset.as_view()),
    path('search/',search),
    path('reg/',register),
    path('profile/',profile),
    path('fakepage/',fakepage),
    path('payment/',pay),
    path('upi/',upi),
]