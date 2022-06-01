from django.contrib import admin

# Register your models here.

from .models import FacePattern,Student,Attendance,Classes,Staff,Subject,Course,Announcement


admin.site.register(FacePattern)
admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(Classes)
admin.site.register(Staff)
admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(Announcement)
