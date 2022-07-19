from rest_framework import serializers

from .models import StudentModel, NotificationModel, TransactionModel


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = (
            "studentId",
            "name",
            "phone",
            "gender",
            "father",
            "mother",
            "address",
            "group",
            "age",
            "dob",
            "speechTherapy",
            "therapy",
            "transportation",
            "tuition",
            "snacks",
            "isAdmission",
        )


class NotificationSerializers(serializers.ModelSerializer):
    class Meta:
        model = NotificationModel
        fields = (
            "studentId",
            "transactionId",
            "notificationId",
            "date",
            "amount",
            "month",
            "speechTherapy",
            "therapy",
            "transportation",
            "extras",
            "note",
            "tuition",
            "snacks",
            "paid",
        )


class TransactionSerializers(serializers.ModelSerializer):
    class Meta:
        model = TransactionModel
        fields = (
            "transactionId",
            "date",
            "type",
            "subType",
            "payer",
            "note",
            "amount",
            "mode",
        )
