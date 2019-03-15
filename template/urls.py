from django.urls import path
from . import views

app_name='template'

urlpatterns = [
    path('', views.index , name='index'),
    path('add/' , views.add , name='add'),
    path('info/' , views.info , name='info'),
]