from django.urls import path
from .views import*
app_name = 'teacherapp'
urlpatterns = [
    # path('dash/',dash.as_view(), name = 'dash'),
    path('viewteacher/',viewteacher.as_view(), name = 'teacher_view'),
    path('addteacher/',addteacher.as_view(), name = 'add_teacher'),
    path('updateteacher/<int:pk>',updateteacher.as_view(), name = 'update_teacher'),
    path('delete/<int:pk>',delete.as_view(), name = 'delete'),
    path('tchrdash/',tchrdash.as_view(), name = 'tchrdash'),
    path('choose/',choose.as_view(), name = 'choose'),
    path('addMeterial/',addMeterial.as_view(), name = 'addMeterial'),
    path('meterialview/',meterialview.as_view(), name = 'meterial_view'),
    path('deleteview/<int:pk>',deleteview.as_view(), name = 'deleteview'),
    path('exceldownload/',exceldownload.as_view(), name = 'exceldownload'),
    path('ExportToExcelView/',ExportToExcelView.as_view(), name = 'ExportToExcelView'),
    path('Scoredetailsview/',Scoredetailsview.as_view(), name = 'Scoredetailsview'),
    path('Scoredetailsviewadd/',Scoredetailsviewadd.as_view(), name = 'Scoredetailsviewadd'),
    path('updatemark<int:pk>/',updatemark.as_view(), name = 'updatemark'),
    path('deleteviewscore<int:pk>/',deleteviewscore.as_view(), name = 'deleteviewscore'),
    path('attandenceview/',attandenceview.as_view(), name = 'attandenceview'),
    path('attandencelistview/',attandencelistview.as_view(), name = 'attandencelistview'),
    path('updateattandenceview/<int:pk>',updateattandenceview.as_view(), name = 'updateattandenceview'),
    path('delete_attandenceview/<int:pk>',delete_attandenceview.as_view(), name = 'delete_attandenceview'),
    
]