from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Batch)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Achivments)
admin.site.register(attandence1)
admin.site.register(importex,ImportExportModelAdmin)
admin.site.register(imageuploder1)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(student_detail)

