from django.urls import path
from .views import *
from .import views
from .import *

urlpatterns = [

    path('',views.index, name = 'index'),
    path('RedirecttoRegistratio/',RedirecttoRegistration.as_view(), name = 'RedirecttoRegistratio'),
    path('Registraion1/',Registraion1.as_view(), name = 'Registraion1'),
    path('Registraion3/',Registraion3.as_view(), name = 'Registraion3'),
    path('AdminLoginView/',AdminLoginView.as_view(), name = 'admin_login'),
    path('TeacherLoginView/',TeacherLoginView.as_view(), name = 'teacher_login'),
    path('StudentLoginView/',StudentLoginView.as_view(), name = 'student_login'),
    path('otp_email/',otp_email.as_view(), name = 'otp_email'),
    path('otp_varification/',otp_verification.as_view(), name = 'otp_varification'),
    path('studentview/',studentview.as_view(), name = 'studentview'),
    path('imageviewer/',imageviewer.as_view(), name = 'imageviewer'),
    path('imageadder/',imageadder.as_view(), name = 'imageadder'),
    path('imageeditor/<int:pk>',imageeditor.as_view(), name = 'imageeditor'),
    path('imagedelete/<int:pk>',imagedelete.as_view(), name = 'imagedelete'),
    path('get-states/', GetStatesView.as_view(), name='get_states'),
    path('get-cities/', GetCitiesView.as_view(), name='get_cities'),
    path('student-detail/', StudentDetailView.as_view(), name='student_detail_view'),
    path('student-detail/', StudentDetailView.as_view(), name='student_detail_view'),
    # path('djangocaptchaView/', djangocaptchaView.as_view(), name='djangocaptchaView'),
    


]
