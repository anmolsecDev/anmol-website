from django.test import TestCase
from .models import Event
from datetime import datetime

# Create your tests here.


class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Event()
        first_item.event = "the first ever event"
        first_item.body = "the first ever event body"
        first_item.date = "2022-10-02"
        first_item.password = "yY3mzS^95O2c#^P"
        first_item.save()

        second_item = Event()
        second_item.event = "the second event"
        second_item.body = "the second event body"
        second_item.date = "2022-10-02"
        second_item.password = "yY3mzS^95O2c#^P"
        second_item.save()

        saved_items = Event.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]

        self.assertEqual(first_saved_item.event, "the first ever event")
        self.assertEqual(first_saved_item.body, "the first ever event body")
        self.assertEqual(second_saved_item.event, "the second event")
        self.assertEqual(second_saved_item.body, "the second event body")


class NewItemTest(TestCase):
    def test_can_save_a_POST_request(self):
        self.client.post(
            "/events/new",
            data={
                "event_text": "A new event for event",
                "body_text": "A new body for event",
                "date_text": "2022-10-04",
                "password": "yY3mzS^95O2c#^P",
            },
        )
        self.assertEqual(Event.objects.count(), 1)

        new_item = Event.objects.first()
        self.assertEqual(new_item.event, "A new event for event")
        self.assertEqual(new_item.body, "A new body for event")
        self.assertEqual(
            new_item.date.strftime("%Y-%m-%d"),
            "2022-10-04",
        )

    def test_can_redirect_after_POST(self):
        response = self.client.post(
            "/events/new",
            data={
                "event_text": "A new event for event",
                "body_text": "A new body for event",
                "date_text": "2022-10-4",
                "password": "yY3mzS^95O2c#^P",
            },
        )
        self.assertRedirects(response, "/events/")


class EventPageTest(TestCase):
    def test_event_page_returns_correct_html(self):
        response = self.client.get("/events/")
        self.assertTemplateUsed(response, "events.html")

    def test_multiple_items_view(self):
        Event.objects.create(
            event="event1",
            body="body1",
            date="2022-12-01",
        )
        Event.objects.create(
            event="event2",
            body="body2",
            date="2022-05-05",
        )

        response = self.client.get("/events/")
        response_text = response.content.decode()
        self.assertIn("event1", response_text)
        self.assertIn("event2", response_text)
        self.assertIn("body1", response_text)
        self.assertIn("body2", response_text)


class EventGetAPITest(TestCase):
    def test_can_get_latest_event(self):
        new_event = Event()
        new_event.event = "the first ever event"
        new_event.body = "the first ever event body"

        year, month, day = list(map(int, datetime.now().strftime("%Y %m %d").split()))
        year += 2
        new_event.date = "-".join([str(year), str(month).zfill(2), str(day)])
        checkDate = new_event.date
        new_event.save()

        self.assertEqual(Event.objects.count(), 1)

        response = self.client.get("/events/getEvent/")
        decoded = response.json()[0]
        self.assertEqual(decoded["date"], checkDate)
        self.assertEqual(decoded["event"], "the first ever event")
        self.assertEqual(decoded["body"], "the first ever event body")
