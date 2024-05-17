from django.urls import path
from .views import *
from .import views
app_name = 'courseapp'

urlpatterns = [

    
    path('viewCourse/',viewCourse.as_view(), name = 'course_view'),
    path('addcourse/',addcourse.as_view(), name = 'add_course'),
    path('updatecourse/<int:pk>',updatecourse.as_view(), name = 'update_course'),
    path('delete/<int:pk>',delete.as_view(), name = 'delete'),

]
