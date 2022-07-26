from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from apis.models import StudentModel
from apis.serializers import StudentSerializers

from apis.models import TransactionModel
from apis.serializers import TransactionSerializers

from apis.models import NotificationModel
from apis.serializers import NotificationSerializers

from apis.models import AccountModel
from apis.serializers import AccountModelSerializers

from apis.models import Assets
from apis.serializers import AssetsModelSerializers

from apis.models import Liabilities
from apis.serializers import LiabilitiesModelSerializers

from apis.models import TrialBalanceModel
from apis.serializers import TrialBalanceModelSerializers

from rest_framework.decorators import api_view
import nepali_datetime


def transaction_maintainer(transaction_id):
    stored_transaction = TransactionModel.objects.all().filter(
        transactionId__icontains=transaction_id
    )[0]
    amount = int(stored_transaction.amount)
    paidFrom = stored_transaction.paidFrom
    paidTo = stored_transaction.paidTo
    mode = stored_transaction.mode
    asset = Assets.objects.first()
    liability = Liabilities.objects.first()

    if paidFrom == "P.T. Cash":
        asset.ptCash -= amount
    elif paidFrom == "Cash Balance":
        asset.cashBalance -= amount
    elif paidFrom == "Borrowing Archana Rimal":
        liability.borrowingArchanaRimal += amount
    elif paidFrom == "Borrowing Sangeeta Neupane":
        liability.borrowingSangeetaNeupane += amount
    elif paidFrom == "Borrowing Others":
        liability.borrowingOthers += amount
        # BANK PAY LEFT

    if paidTo == "P.T. Cash":
        asset.ptCash += amount
    elif paidTo == "Cash Balance":
        asset.cashBalance += amount
    elif paidTo == "Borrowing Archana Rimal":
        liability.borrowingArchanaRimal -= amount
    elif paidTo == "Borrowing Sangeeta Neupane":
        liability.borrowingSangeetaNeupane -= amount
    elif paidTo == "Borrowing Others":
        liability.borrowingOthers -= amount

        # Bank Left

    if mode == "Account Receivable[DO]":
        asset.accountReceivable += amount
    elif mode == "Account Receivable[DONE]":
        asset.accountReceivable -= amount
    elif mode == "Salary Payable[DO]":
        liability.salaryPayable += amount
    elif mode == "Salary Payable[DONE]":
        liability.salaryPayable -= amount
    elif mode == "Audit Fee Payable[DO]":
        liability.auditFeePayable += amount
    elif mode == "Audit Fee Payable[DONE]":
        liability.auditFeePayable -= amount
    elif mode == "Other Payable[DO]":
        liability.otherPayable += amount
    elif mode == "Other Payable[DONE]":
        liability.otherPayable -= amount

    asset.save()
    liability.save()


@api_view(["GET", "POST"])
def student_list(request):
    if request.method == "GET":
        students = StudentModel.objects.all()
        studentId = request.GET.get("studentId", None)
        if studentId is not None:
            students = students.filter(studentId__icontains=studentId)
        student_serializer = StudentSerializers(students, many=True)
        return JsonResponse(student_serializer.data, safe=False)

    elif request.method == "POST":
        student_data = JSONParser().parse(request)
        student_serializer = StudentSerializers(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse(student_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(
            student_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET", "PUT", "DELETE"])
def student_detail(request, studentId):
    try:
        student = StudentModel.objects.get(pk=studentId)
    except StudentModel.DoesNotExist:
        return JsonResponse(
            {"message": "The student does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":
        student_serializer = StudentSerializers(student)
        return JsonResponse(student_serializer.data)

    elif request.method == "PUT":
        student_data = JSONParser().parse(request)
        student_serializer = StudentSerializers(student, data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse(student_serializer.data)
        return JsonResponse(
            student_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
    elif request.method == "DELETE":
        student.delete()
        return JsonResponse(
            {"message": "Student data was deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )


@api_view(["GET", "POST"])
def notification_list(request):
    if request.method == "GET":
        notifications = NotificationModel.objects.all()
        studentId = request.GET.get("studentId", None)
        if studentId is not None:
            notifications = notifications.filter(studentId__icontains=studentId)
        notification_serializer = NotificationSerializers(notifications, many=True)
        return JsonResponse(notification_serializer.data, safe=False)

    elif request.method == "POST":
        notification_data = JSONParser().parse(request)
        notification_serializer = NotificationSerializers(data=notification_data)
        if notification_serializer.is_valid():
            notification_serializer.save()
            return JsonResponse(
                notification_serializer.data, status=status.HTTP_201_CREATED
            )
        return JsonResponse(
            notification_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET", "PUT", "DELETE"])
def notification_detail(request, notificationId):
    try:
        notification = NotificationModel.objects.get(pk=notificationId)

    except NotificationModel.DoesNotExist:
        return JsonResponse(
            {"message": "The notification does not exist"},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "GET":
        notification_serializer = NotificationSerializers(notification)
        return JsonResponse(notification_serializer.data)

    elif request.method == "PUT":
        notification_data = JSONParser().parse(request)
        notification_serializer = NotificationSerializers(
            notification, data=notification_data
        )
        if notification_serializer.is_valid():
            notification_serializer.save()
            return JsonResponse(notification_serializer.data)
        return JsonResponse(
            notification_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
    elif request.method == "DELETE":
        notification.delete()
        return JsonResponse(
            {"message": "Notification data was deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )


@api_view(["GET", "POST"])
def transaction_list(request):
    if request.method == "GET":
        transactions = TransactionModel.objects.all()
        transaction_serializer = TransactionSerializers(transactions, many=True)
        return JsonResponse(transaction_serializer.data, safe=False)

    elif request.method == "POST":
        transaction_data = JSONParser().parse(request)

        transaction_serializer = TransactionSerializers(data=transaction_data)
        if transaction_serializer.is_valid():
            transaction_id = transaction_data["transactionId"]
            transaction_serializer.save()
            transaction_maintainer(transaction_id)
            return JsonResponse(
                transaction_serializer.data, status=status.HTTP_201_CREATED
            )
        return JsonResponse(
            transaction_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET", "PUT", "DELETE"])
def transaction_detail(request, transactionId):
    try:
        transaction = TransactionModel.objects.get(pk=transactionId)
    except TransactionModel.DoesNotExist:
        return JsonResponse(
            {"message": "The transaction does not exist"},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "GET":
        transaction_serializer = TransactionSerializers(transaction)
        return JsonResponse(transaction_serializer.data)

    elif request.method == "PUT":
        transaction_data = JSONParser().parse(request)
        transaction_serializer = TransactionSerializers(
            transaction, data=transaction_data
        )
        if transaction_serializer.is_valid():
            transaction_serializer.save()
            return JsonResponse(transaction_serializer.data)
        return JsonResponse(
            transaction_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
    elif request.method == "DELETE":
        transaction.delete()
        return JsonResponse(
            {"message": "Transaction data was deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )


@api_view(["GET"])
def fee_status(request, studentId):

    months = {
        "Baisakh": 1,
        "Jestha": 2,
        "Ashar": 3,
        "Shrawan": 4,
        "Bhadra": 5,
        "Ashoj": 6,
        "Kartik": 7,
        "Mangsir": 8,
        "Paush": 9,
        "Magh": 10,
        "Falgun": 11,
        "Chaitra": 12,
    }

    if studentId is not None:
        notifications = NotificationModel.objects.all()
        notifications = notifications.filter(studentId__icontains=studentId)
        current_year = nepali_datetime.datetime.now().year
        current_month = nepali_datetime.datetime.now().month
        notifications = notifications.filter(year__icontains=current_year)
        if (len(notifications)) != 0:
            latest = max([months[i.month] for i in notifications])
            if latest == current_month:
                return JsonResponse(data={"status": "paid"})
        return JsonResponse(data={"status": "unpaid"})
    else:
        return JsonResponse(
            {"message": "StudentId not valid"}, status=status.HTTP_404_NOT_FOUND
        )


@api_view(["GET"])
def account_list(request):
    if request.method == "GET":
        accounts = AccountModel.objects.all()
        account_serializer = AccountModelSerializers(accounts, many=True)
        return JsonResponse(account_serializer.data, safe=False)

    if request.method == "POST":
        account_data = JSONParser().parse(request)
        account_serializer = AccountModelSerializers(data=account_data)
        if account_serializer.is_valid():
            account_serializer.save()
            return JsonResponse(account_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(
            account_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET"])
def asset_list(request):
    asset = Assets.objects.all()
    assets_serializer = AssetsModelSerializers(asset, many=True)
    return JsonResponse(assets_serializer.data, safe=False)


@api_view(["GET"])
def liability_list(request):
    liability = Liabilities.objects.all()
    liability_serializer = LiabilitiesModelSerializers(liability, many=True)
    return JsonResponse(liability_serializer.data, safe=False)


@api_view(["GET", "POST"])
def trial_balance_list(request):
    if request.method == "GET":
        trialBalances = TrialBalanceModel.objects.all()
        trialBalance_serializer = TrialBalanceModelSerializers(trialBalances, many=True)
        return JsonResponse(trialBalance_serializer.data, safe=False)

    elif request.method == "POST":
        trialBalance_data = JSONParser().parse(request)

        trialBalance_serializer = TrialBalanceModelSerializers(data=trialBalance_data)
        if trialBalance_serializer.is_valid():
            trialBalance_serializer.save()
            return JsonResponse(
                trialBalance_serializer.data, status=status.HTTP_201_CREATED
            )
        return JsonResponse(
            trialBalance_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET"])
def trial_balance_create(request):
    newtb = TrialBalanceModel.objects.create(trailBalanceId="dsnj8n22dfdaasdffcekdn")
    newtb.year = 2079
    newtb.month = 8
    newtb.save()
    newtb_serializer = TrialBalanceModelSerializers(newtb)
    return JsonResponse(newtb_serializer.data)
