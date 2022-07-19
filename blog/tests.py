from django.test import TestCase
from blog.models import Blog

# Create your tests here.


class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Blog()
        first_item.title = "the first ever blog"
        first_item.body = "the first ever blog body"
        first_item.date = "2022-10-02"
        first_item.password = "yY3mzS^95O2c#^P"
        first_item.save()

        second_item = Blog()
        second_item.title = "the second blog"
        second_item.body = "the second blog body"
        second_item.date = "2022-10-02"
        second_item.password = "yY3mzS^95O2c#^P"
        second_item.save()

        saved_items = Blog.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]

        self.assertEqual(first_saved_item.title, "the first ever blog")
        self.assertEqual(first_saved_item.body, "the first ever blog body")
        self.assertEqual(second_saved_item.title, "the second blog")
        self.assertEqual(second_saved_item.body, "the second blog body")


class NewItemTest(TestCase):
    def test_can_save_a_POST_request(self):
        self.client.post(
            "/blogs/new",
            data={
                "title_text": "A new title for blog",
                "body_text": "A new body for blog",
                "date_text": "2022-10-04",
                "password": "yY3mzS^95O2c#^P",
            },
        )
        self.assertEqual(Blog.objects.count(), 1)

        new_item = Blog.objects.first()
        self.assertEqual(new_item.title, "A new title for blog")
        self.assertEqual(new_item.body, "A new body for blog")
        self.assertEqual(
            new_item.date.strftime("%Y-%m-%d"),
            "2022-10-04",
        )

    def test_can_redirect_after_POST(self):
        response = self.client.post(
            "/blogs/new",
            data={
                "title_text": "A new title for blog",
                "body_text": "A new body for blog",
                "date_text": "2022-10-4",
                "password": "yY3mzS^95O2c#^P",
            },
        )
        self.assertRedirects(response, "/blogs/")


class BlogPageTest(TestCase):
    def test_blog_page_returns_correct_html(self):
        response = self.client.get("/blogs/")
        self.assertTemplateUsed(response, "blogs.html")

    def test_multiple_items_view(self):
        Blog.objects.create(
            title="title1",
            body="body1",
            date="2022-12-01",
        )
        Blog.objects.create(
            title="title2",
            body="body2",
            date="2022-05-05",
        )

        response = self.client.get("/blogs/")
        response_text = response.content.decode()
        self.assertIn("title1", response_text)
        self.assertIn("title2", response_text)
        self.assertIn("body1", response_text)
        self.assertIn("body2", response_text)
