from django.test import TestCase


# Create your tests here.
class PageTemplateRenderTest(TestCase):
    def test_for_homepage(self):
        response = self.client.get("")
        self.assertTemplateUsed(response, "homepage.html")

    def test_for_about(self):
        response = self.client.get("/about")
        self.assertTemplateUsed(response, "about.html")

    def test_for_donate(self):
        response = self.client.get("/donate")
        self.assertTemplateUsed(response, "donate.html")

    def test_for_contact(self):
        response = self.client.get("/contact")
        self.assertTemplateUsed(response, "contact.html")
