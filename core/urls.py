from django.urls import path 
from .views import *

urlpatterns = [
    

    path('LandPlotAPIView', LandPlotAPIView.as_view(), name='home')
]


