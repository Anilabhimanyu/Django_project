from django.urls import path
from Courses.views import courseListDelete,courseListInsert,courseListUpdate,courseListView

urlpatterns={
    path('courselistview',courseListView,name="courselistview"),
    path('courselistinsert',courseListInsert,name="courselistinsert"),
    path('courselistupdate/<course_id>',courseListUpdate,name="courselistupdate"),
    path("courselistdelete/<course_id>",courseListDelete,name="courselistdelete"),    
}
