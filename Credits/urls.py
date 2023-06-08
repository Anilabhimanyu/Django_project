from django.urls import path,include
from Credits.views import CreditsListView

urlpatterns={
    path('creditview',CreditsListView.as_view(),name="creditview"),
}