from django.test import TestCase
from .models import NotificationModel, StudentModel, TransactionModel

# Create your tests here.


class NewStudentTest(TestCase):
    def test_can_save_a_POST_request(self):
        response = self.client.post(
            path="/api/student/",
            data={
                "studentId": "asectyler4a10b",
                "name": "Tyler Matther",
                "phone": 9991327884,
                "gender": "M",
                "father": "Burton Maldonado",
                "mother": "Misty Gardner",
                "address": "Bloomington, Mali",
                "group": "D",
                "age": 3,
                "dob": "2017/7/20",
                "speechTherapy": 4000,
                "therapy": 0,
                "transportation": 0,
                "tuition": 8000,
                "snacks": 0,
                "isAdmission": True,
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(StudentModel.objects.count(), 1)
        new_student = StudentModel.objects.first()
        self.assertEqual(new_student.studentId, "asectyler4a10b")

    def test_student_model(self):
        first_obj = StudentModel.objects.create(
            studentId="asectyler4a10b",
            name="Tyler Matther",
            phone=9991327884,
            gender="M",
            father="Burton Maldonado",
            mother="Misty Gardner",
            address="Bloomington, Mali",
            group="D",
            age=3,
            dob="2017/7/20",
            speechTherapy=4000,
            therapy=0,
            transportation=0,
            tuition=8000,
            snacks=0,
            isAdmission=True,
        )
        second_obj = StudentModel.objects.create(
            studentId="asecaaryan4a10b",
            name="Tyler Matthew",
            phone=9991327884,
            gender="M",
            father="Burton Maldonado",
            mother="Misty Gardner",
            address="Bloomington, Mali",
            group="D",
            age=10,
            dob="2017/7/20",
            speechTherapy=4000,
            therapy=0,
            transportation=0,
            tuition=8000,
            snacks=0,
            isAdmission=True,
        )
        # first_obj = StudentModel.objects.first()
        # second_obj = StudentModel.objects.last()

        self.assertEqual(first_obj.name, "Tyler Matther")
        self.assertEqual(second_obj.name, "Tyler Matthew")
        self.assertEqual(first_obj.age, 3)
        self.assertEqual(second_obj.age, 10)

    def test_can_get_list_of_all_students(self):
        first_obj = StudentModel.objects.create(
            studentId="asectyler4a10b",
            name="Tyler Matther",
            phone=9991327884,
            gender="M",
            father="Burton Maldonado",
            mother="Misty Gardner",
            address="Bloomington, Mali",
            group="D",
            age=3,
            dob="2017/7/20",
            speechTherapy=4000,
            therapy=0,
            transportation=0,
            tuition=8000,
            snacks=0,
            isAdmission=True,
        )
        second_obj = StudentModel.objects.create(
            studentId="asecaaryan4a10b",
            name="Tyler Matthew",
            phone=9991327884,
            gender="M",
            father="Burton Maldonado",
            mother="Misty Gardner",
            address="Bloomington, Mali",
            group="D",
            age=10,
            dob="2017/7/20",
            speechTherapy=4000,
            therapy=0,
            transportation=0,
            tuition=8000,
            snacks=0,
            isAdmission=True,
        )

        response = self.client.get("/api/student/").json()
        stored_first_obj = response[0]
        stored_second_obj = response[1]
        self.assertEqual(first_obj.name, stored_first_obj["name"])
        self.assertEqual(second_obj.name, stored_second_obj["name"])
        self.assertEqual(first_obj.age, stored_first_obj["age"])
        self.assertEqual(second_obj.age, stored_second_obj["age"])

    def test_can_handle_GET_request_for_single_student(self):
        testStudentId = "asectyler4a10b"
        testAddress = "Bloomington, Mali"

        response = self.client.post(
            "/api/student/",
            data={
                "studentId": testStudentId,
                "name": "Tyler Matther",
                "phone": 9991327884,
                "gender": "M",
                "father": "Burton Maldonado",
                "mother": "Misty Gardner",
                "address": testAddress,
                "group": "D",
                "age": 3,
                "dob": "2017/7/20",
                "speechTherapy": 4000,
                "therapy": 0,
                "transportation": 0,
                "tuition": 8000,
                "snacks": 0,
                "isAdmission": True,
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(StudentModel.objects.count(), 1)
        new_student = self.client.get("/api/student/details/" + testStudentId).json()

        self.assertEqual(new_student["studentId"], testStudentId)
        self.assertEqual(new_student["address"], testAddress)

    def test_can_update_data(self):
        testStudentId = "asectyler4a10b"
        testAddress = "Bloomington, Mali"
        self.client.post(
            "/api/student/",
            data={
                "studentId": testStudentId,
                "name": "Tyler Matther",
                "phone": 9991327884,
                "gender": "M",
                "father": "Burton Maldonado",
                "mother": "Misty Gardner",
                "address": testAddress,
                "group": "D",
                "age": 3,
                "dob": "2017/7/20",
                "speechTherapy": 4000,
                "therapy": 0,
                "transportation": 0,
                "tuition": 8000,
                "snacks": 0,
                "isAdmission": True,
            },
            content_type="application/json",
        )
        self.client.put(
            "/api/student/details/" + testStudentId,
            data={
                "studentId": testStudentId,
                "name": "Tyler Matthew",
                "phone": 9991327884,
                "gender": "M",
                "father": "Burton Maldonado",
                "mother": "Misty Gardner",
                "address": testAddress,
                "group": "D",
                "age": 3,
                "dob": "2017/7/20",
                "speechTherapy": 4000,
                "therapy": 0,
                "transportation": 0,
                "tuition": 8000,
                "snacks": 0,
                "isAdmission": True,
            },
            content_type="application/json",
        )
        response = self.client.get("/api/student/details/" + testStudentId)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(StudentModel.objects.count(), 1)
        changed_record = response.json()
        self.assertEqual(changed_record["name"], "Tyler Matthew")
        self.assertEqual(changed_record["gender"], "M")

    def test_can_delete_a_record(self):
        testStudentId = "asectyler4a10b"
        self.client.post(
            "/api/student/",
            data={
                "studentId": testStudentId,
                "name": "Tyler Matther",
                "phone": 9991327884,
                "gender": "M",
                "father": "Burton Maldonado",
                "mother": "Misty Gardner",
                "address": "Bloomington, Mali",
                "group": "D",
                "age": 3,
                "dob": "2017/7/20",
                "speechTherapy": 4000,
                "therapy": 0,
                "transportation": 0,
                "tuition": 8000,
                "snacks": 0,
                "isAdmission": True,
            },
            content_type="application/json",
        )
        self.assertEqual(StudentModel.objects.count(), 1)
        self.client.delete("/api/student/details/" + testStudentId)
        self.assertEqual(StudentModel.objects.count(), 0)


class NewNotificationTest(TestCase):
    def test_can_save_a_POST_request(self):

        studentId = "asectyler4a10b"
        response = self.client.post(
            path="/api/notification/",
            data={
                "studentId": studentId,
                "transactionId": "1O9V8D55",
                "notificationid": "62D16D94BDB55F7BDDD913A3",
                "date": "2022/2/27",
                "paid": "Cash",
                "amount": 14000,
                "month": "Ashar",
                "speechTherapy": 0,
                "therapy": 4000,
                "transportation": 800,
                "extras": 100,
                "note": "Picnic Charge",
                "tuition": 8000,
                "snacks": 450,
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(NotificationModel.objects.count(), 1)
        new_notification = NotificationModel.objects.first()
        self.assertEqual(new_notification.amount, 14000)

    def test_can_handle_GET_request_for_details(self):
        testNotificationId = "62D16D94BDB55F7BDDD913A3"

        response = self.client.post(
            "/api/notification/",
            data={
                "studentId": "asectyler4a10b",
                "transactionId": "1O9V8D55",
                "notificationId": testNotificationId,
                "date": "2022/2/27",
                "paid": "Cash",
                "amount": 14000,
                "month": "Ashar",
                "speechTherapy": 0,
                "therapy": 4000,
                "transportation": 800,
                "extras": 100,
                "note": "Picnic Charge",
                "tuition": 8000,
                "snacks": 450,
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(NotificationModel.objects.count(), 1)
        new_notification = self.client.get(
            "/api/notification/details/" + testNotificationId
        ).json()
        self.assertEqual(new_notification["studentId"], "asectyler4a10b")
        self.assertEqual(new_notification["amount"], 14000)

    def test_can_handle_GET_request_for_all_notification_of_a_student(self):
        testStudentId = "asectyler4a10b"

        response = self.client.post(
            "/api/notification/",
            data={
                "studentId": testStudentId,
                "transactionId": "1O9V8D55",
                "notificationId": "62D16D94BDB55F7BDDD914A6",
                "date": "2022/2/27",
                "amount": 14000,
                "month": "Jestha",
                "speechTherapy": 0,
                "therapy": 4000,
                "transportation": 800,
                "extras": 100,
                "note": "Picnic Charge",
                "tuition": 8000,
                "snacks": 450,
                "paid": "Cash",
            },
            content_type="application/json",
        )
        self.assertEqual(NotificationModel.objects.count(), 1)
        self.assertEqual(response.status_code, 201)

        response = self.client.post(
            "/api/notification/",
            data={
                "studentId": testStudentId,
                "transactionId": "1O9V8D65",
                "notificationId": "62D16D9478755F7BDDD913A5",
                "date": "2022/3/27",
                "paid": "Cash",
                "amount": 12000,
                "month": "Ashar",
                "speechTherapy": 0,
                "therapy": 4000,
                "transportation": 800,
                "extras": 0,
                "note": " ",
                "tuition": 8000,
                "snacks": 450,
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(NotificationModel.objects.count(), 2)

        all_notifications = self.client.get(
            "/api/notification/", data={"studentId": testStudentId}
        ).json()
        self.assertEqual(len(all_notifications), 2)
        counter = 0
        for items in all_notifications:
            if items["extras"] == 100 or items["extras"] == 0:
                counter += 1

        self.assertEqual(counter, 2)

    def test_can_update_data(self):

        testNotificationId = "62D16D94BDB55F7BDDD913A3"

        self.client.post(
            "/api/notification/",
            data={
                "studentId": "asectyler4a10b",
                "transactionId": "1O9V8D55",
                "notificationId": testNotificationId,
                "date": "2022/2/27",
                "paid": "Cash",
                "amount": 14000,
                "month": "Ashar",
                "speechTherapy": 0,
                "therapy": 1000,
                "transportation": 800,
                "extras": 100,
                "note": "Picnic Charge",
                "tuition": 8000,
                "snacks": 450,
            },
            content_type="application/json",
        )

        self.assertEqual(NotificationModel.objects.count(), 1)
        self.client.put(
            "/api/notification/details/" + testNotificationId,
            data={
                "studentId": "asectyler4a10b",
                "transactionId": "1O9V8D55",
                "notificationId": testNotificationId,
                "date": "2022/2/27",
                "paid": "Cash",
                "amount": 13000,
                "month": "Ashar",
                "speechTherapy": 0,
                "therapy": 4000,
                "transportation": 800,
                "extras": 0,
                "note": "",
                "tuition": 8000,
                "snacks": 450,
            },
            content_type="application/json",
        )
        try:
            response = NotificationModel.objects.get(pk=testNotificationId)
        except NotificationModel.DoesNotExist:
            self.fail(msg="No notification Found")
        response = self.client.get("/api/notification/details/" + testNotificationId)
        self.assertEqual(response.status_code, 200)
        changed_record = response.json()
        self.assertEqual(changed_record["therapy"], 4000)
        self.assertEqual(changed_record["note"], "")
        self.assertEqual(changed_record["extras"], 0)

    def test_can_delete_a_record(self):

        testNotificationId = "62D16D94BDB55F7BDDD913A3"
        self.client.post(
            "/api/notification/",
            data={
                "studentId": "asectyler4a10b",
                "transactionId": "1O9V8D55",
                "notificationId": testNotificationId,
                "date": "2022/2/27",
                "paid": "Cash",
                "amount": 13000,
                "month": "Ashar",
                "speechTherapy": 0,
                "therapy": 4000,
                "transportation": 800,
                "extras": 0,
                "note": "",
                "tuition": 8000,
                "snacks": 450,
            },
            content_type="application/json",
        )
        self.assertEqual(NotificationModel.objects.count(), 1)
        self.client.delete("/api/notification/details/" + testNotificationId)
        self.assertEqual(NotificationModel.objects.count(), 0)


class NewTransactionTest(TestCase):
    def test_can_save_a_POST_request(self):
        response = self.client.post(
            path="/api/transaction/",
            data={
                "transactionId": "62D3F6C50221C0F74A88BDBA",
                "date": "2022/3/21",
                "type": "Salary",
                "subType": "Student",
                "payer": "Bond Alexander",
                "note": "Sit incididunt duis tempor eiusmod eu dolore ipsum ex aliquip.",
                "amount": 14000,
                "mode": "credit",
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(TransactionModel.objects.count(), 1)
        new_transaction = TransactionModel.objects.first()
        self.assertEqual(new_transaction.amount, 14000)

    def test_can_get_list_of_all_transaction(self):
        first_obj = TransactionModel.objects.create(
            transactionId="62D3F6C50221C0F74A88BDBA",
            date="2022/3/21",
            type="Salary",
            subType="Student",
            payer="Bond James",
            note="Sit incididunt duis tempor eiusmod eu dolore ipsum ex aliquip.",
            amount=14000,
            mode="credit",
        )
        second_obj = TransactionModel.objects.create(
            transactionId="62D3F6C50221C0F7T5Y8BDBA",
            date="2022/3/21",
            type="Salary",
            subType="Student",
            payer="Bond Alexander",
            note="Sit incididunt duis tempor eiusmod eu dolore ipsum ex aliquip.",
            amount=14000,
            mode="credit",
        )

        response = self.client.get("/api/transaction/").json()
        stored_first_obj = response[0]
        stored_second_obj = response[1]
        self.assertEqual(first_obj.payer, stored_first_obj["payer"])
        self.assertEqual(second_obj.payer, stored_second_obj["payer"])
        self.assertEqual(first_obj.amount, stored_first_obj["amount"])
        self.assertEqual(second_obj.amount, stored_second_obj["amount"])

    def test_can_handle_GET_request_for_details(self):
        testTransactionId = "62D16D94BDB55F7BDDD913A3"

        response = self.client.post(
            "/api/transaction/",
            data={
                "transactionId": testTransactionId,
                "date": "2022/3/21",
                "type": "salary",
                "subType": "student",
                "payer": "Bond Alexander",
                "note": "Sit incididunt duis tempor eiusmod eu dolore ipsum ex aliquip.",
                "amount": 14000,
                "mode": "credit",
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(TransactionModel.objects.count(), 1)
        new_transaction = self.client.get(
            "/api/transaction/details/" + testTransactionId
        ).json()
        self.assertEqual(new_transaction["type"], "salary")
        self.assertEqual(new_transaction["mode"], "credit")

    def test_can_update_data(self):

        testTransactionId = "62D16D94BDB55F7BDDD913A3"

        self.client.post(
            "/api/transaction/",
            data={
                "transactionId": testTransactionId,
                "date": "2022/3/21",
                "type": "salary",
                "subType": "student",
                "payer": "Bond Alexander",
                "note": "Sit incididunt duis tempor eiusmod eu dolore ipsum ex aliquip.",
                "amount": 14000,
                "mode": "credit",
            },
            content_type="application/json",
        )

        self.assertEqual(TransactionModel.objects.count(), 1)
        self.client.put(
            "/api/transaction/details/" + testTransactionId,
            data={
                "transactionId": testTransactionId,
                "date": "2022/3/21",
                "type": "salary",
                "subType": "student",
                "payer": "Bond Alexander",
                "note": "Sit incididunt duis tempor eiusmod eu dolore ipsum ex aliquip.",
                "amount": 12000,
                "mode": "credit",
            },
            content_type="application/json",
        )
        try:
            response = TransactionModel.objects.get(pk=testTransactionId)
        except TransactionModel.DoesNotExist:
            self.fail(msg="No transaction Found")
        response = self.client.get("/api/transaction/details/" + testTransactionId)
        self.assertEqual(response.status_code, 200)
        changed_record = response.json()
        self.assertEqual(changed_record["amount"], 12000)

    def test_can_delete_a_record(self):

        testTransactionId = "62D16D94BDB55F7BDDD913A3"
        self.client.post(
            "/api/transaction/",
            data={
                "transactionId": testTransactionId,
                "date": "2022/3/21",
                "type": "salary",
                "subType": "student",
                "payer": "Bond Alexander",
                "note": "Sit incididunt duis tempor eiusmod eu dolore ipsum ex aliquip.",
                "amount": 14000,
                "mode": "credit",
            },
            content_type="application/json",
        )
        self.assertEqual(TransactionModel.objects.count(), 1)
        self.client.delete("/api/transaction/details/" + testTransactionId)
        self.assertEqual(TransactionModel.objects.count(), 0)
