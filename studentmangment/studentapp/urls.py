from django.urls import path
from .views import *
from .import views

urlpatterns = [

    path('',views.index, name = 'index'),
    path('RedirecttoRegistratio/',RedirecttoRegistration.as_view(), name = 'RedirecttoRegistratio'),
    path('Registraion1/',Registraion1.as_view(), name = 'Registraion1'),
    # path('Registraion2/',Registraion2.as_view(), name = 'Registraion2'),
    path('Registraion3/',Registraion3.as_view(), name = 'Registraion3'),
    path('AdminLoginView/',AdminLoginView.as_view(), name = 'admin_login'),
    path('TeacherLoginView/',TeacherLoginView.as_view(), name = 'teacher_login'),
    path('StudentLoginView/',StudentLoginView.as_view(), name = 'student_login'),
    path('otp_email/',otp_email.as_view(), name = 'otp_email'),
    path('otp_varification/',otp_verification.as_view(), name = 'otp_varification'),
    


]
