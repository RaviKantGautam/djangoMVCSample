from django.urls import path,include
from .views import *

app_name = 'post'

urlpatterns = [
    path('demo/',snipview.as_view(),name='demo'),
    path('snippdetail/<pk>/',snippdetail.as_view(),name='snippdetail'),
    path('snippupdate/<pk>/',snippupdate.as_view(),name='snippupdate'),
    path('snippdelete/<pk>/',snippdelete.as_view(),name='snippdelete'),
    path('snippcreateview/',snippcreateview.as_view(),name='snippcreateview'),
]
