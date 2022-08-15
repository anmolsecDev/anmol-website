from rest_framework import serializers

from .models import (
    Assets,
    Liabilities,
    StudentModel,
    NotificationModel,
    TransactionModel,
    AccountModel,
)


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
            "year",
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
            "paidTo",
            "paidFrom",
            "mode",
            "payer",
            "note",
            "amount",
        )


class AccountModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = AccountModel
        fields = ("accountId", "name", "currBalance", "bankName", "currLoan")


class AssetsModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Assets
        fields = ("cashBalance", "ptCash", "accountReceivable")


class LiabilitiesModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Liabilities
        fields = (
            "shareCapitalArchana",
            "shareCapitalSangita",
            "borrowingLoanBank",
            "borrowingArchanaRimal",
            "borrowingSangeetaNeupane",
            "borrowingOthers",
            "socialSecurityTax",
            "salaryTax",
            "salaryPayable",
            "auditFeePayable",
            "otherPayable",
            "capitalReserveOrDeficit",
        )
