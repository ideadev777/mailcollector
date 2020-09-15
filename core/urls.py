from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('ajaxtest/', views.AjaxTest , name='ajaxtest'),
    path('search/', views.Search.as_view(), name='search'),
    path('result/', views.Result.as_view(), name='result'),
 ]