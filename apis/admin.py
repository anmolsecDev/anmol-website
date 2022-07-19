from django.contrib import admin
from .models import StudentModel, NotificationModel

# Register your models here.

admin.site.register(StudentModel)
admin.site.register(NotificationModel)
