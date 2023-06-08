from django.urls import path
from .views import studlist
urlpatterns={
    path('studlist',studlist,name='studlist'),
}