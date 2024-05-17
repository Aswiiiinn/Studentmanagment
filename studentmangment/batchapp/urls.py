from django.urls import path
from .views import *
from .import views
app_name = 'batchapp'

urlpatterns = [

    
    path('viewbatch/',viewbatch.as_view(), name = 'batch_view'),
    path('addbatch/',addbatch.as_view(), name = 'add_batch'),
    path('updatebatch/<int:pk>',updatebatch.as_view(), name = 'update_batch'),
    path('delete/<int:pk>',delete.as_view(), name = 'delete'),

]
