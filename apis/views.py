from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from apis.models import StudentModel
from apis.serializers import StudentSerializers

from apis.models import TransactionModel
from apis.serializers import TransactionSerializers

from apis.models import NotificationModel
from apis.serializers import NotificationSerializers

from rest_framework.decorators import api_view


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
            transaction_serializer.save()
            return JsonResponse(
                transaction_serializer.data, status=status.HTTP_201_CREATED
            )
        print(transaction_serializer.errors)
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
