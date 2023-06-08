from django.urls import path,include
from .views import student_add,student_delete,student_update,student_view

urlpatterns={
    path("studentadd",student_add,name="studentadd"),
    path("studentview",student_view,name="studentview"),
    path("studentupdate",student_update,name="studentupdate"),
    path("studentdelete",student_delete,name="studentdelete"),
}

