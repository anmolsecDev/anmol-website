from django.contrib import admin
from .models import StudentModel, NotificationModel, TransactionModel

# Register your models here.

admin.site.register(StudentModel)
admin.site.register(NotificationModel)
admin.site.register(TransactionModel)
