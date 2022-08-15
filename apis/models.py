from django.db import models

# Create your models here.


class StudentModel(models.Model):
    studentId = models.CharField(max_length=20, default=0, primary_key=True)
    name = models.CharField(max_length=50, default="")
    phone = models.BigIntegerField(default=0)
    gender = models.CharField(
        max_length=10,
        default="",
        choices=(("M", "Male"), ("F", "Female"), ("O", "Others")),
    )
    father = models.CharField(max_length=50, default="")
    mother = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=100, default="")
    group = models.CharField(max_length=5, default="")
    age = models.IntegerField(default=0)
    dob = models.CharField(max_length=12, default="")
    speechTherapy = models.IntegerField(default=0)
    therapy = models.IntegerField(default=0)
    transportation = models.IntegerField(default=0)
    tuition = models.IntegerField(default=0)
    snacks = models.IntegerField(default=0)
    isAdmission = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class NotificationModel(models.Model):
    studentId = models.CharField(max_length=50, default=0)
    transactionId = models.CharField(max_length=50, default=0)
    notificationId = models.CharField(max_length=50, default=0, primary_key=True)
    date = models.CharField(max_length=15, default="")
    amount = models.IntegerField(default=0)
    month = models.CharField(max_length=20, default="")
    year = models.CharField(max_length=10, default=0)
    speechTherapy = models.IntegerField(default=0)
    therapy = models.IntegerField(default=0)
    transportation = models.IntegerField(default=0)
    extras = models.IntegerField(default=0)
    note = models.CharField(default="", max_length=200, blank=True)
    tuition = models.IntegerField(default=0)
    snacks = models.IntegerField(default=0)
    paid = models.CharField(default="Unpaid", max_length=10)

    def __str__(self):
        return str(self.notificationId)


class TransactionModel(models.Model):
    transactionId = models.CharField(max_length=50, default=0, primary_key=True)
    date = models.CharField(max_length=15, default="")
    type = models.CharField(max_length=20, default="")
    paidTo = models.CharField(max_length=200, default="")
    paidFrom = models.CharField(max_length=200, default="")
    payer = models.CharField(default="", max_length=50)
    note = models.CharField(default="", max_length=200)
    amount = models.IntegerField(default=0)
    mode = models.CharField(default="", max_length=10)

    def __str__(self):
        return str(self.transactionId)


class AccountModel(models.Model):
    accountId = models.CharField(max_length=30, default="", primary_key=True)
    currBalance = models.IntegerField(default=0)
    currLoan = models.IntegerField(default=0)
    bankName = models.CharField(max_length=200, default="")

    def __str__(self):
        return str(self.bankName + " " + "Acc No. " + self.accountId)


class Assets(models.Model):
    cashBalance = models.IntegerField(default=0)
    ptCash = models.IntegerField(default=0)
    accountReceivable = models.IntegerField(default=0)


class Liabilities(models.Model):
    shareCapitalArchana = models.IntegerField(default=0)
    shareCapitalSangita = models.IntegerField(default=0)
    borrowingLoanBank = models.IntegerField(default=0)
    borrowingArchanaRimal = models.IntegerField(default=0)
    borrowingSangeetaNeupane = models.IntegerField(default=0)
    borrowingOthers = models.IntegerField(default=0)
    socialSecurityTax = models.IntegerField(default=0)
    salaryTax = models.IntegerField(default=0)
    salaryPayable = models.IntegerField(default=0)
    auditFeePayable = models.IntegerField(default=0)
    otherPayable = models.IntegerField(default=0)
    capitalReserveOrDeficit = models.IntegerField(default=0)
