from django.contrib import admin
from .models import (
    StudentModel,
    NotificationModel,
    TransactionModel,
    AccountModel,
    Assets,
    Liabilities,
)

# Register your models here.

admin.site.register(StudentModel)
admin.site.register(NotificationModel)
admin.site.register(TransactionModel)
admin.site.register(AccountModel)
admin.site.register(Assets)
admin.site.register(Liabilities)
