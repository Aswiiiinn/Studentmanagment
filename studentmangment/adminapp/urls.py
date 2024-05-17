from django.urls import path
from .views import*
app_name = 'adminapp'
urlpatterns = [
    path('dash/',dash.as_view(), name = 'dash'),
    path('Studentview/',Studentview.as_view(), name = 'index'),
    path('StudentAdd/',StudentAdd.as_view(), name = 'student_add'),
    path('UpdateStudent/<int:pk>',UpdateStudent.as_view(), name = 'update_student'),
    path('DeleteStudent/<int:pk>',DeleteStudent.as_view(), name = 'delete_student'),
]
