from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Batch)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(importex,ImportExportModelAdmin)

