from django.urls import path

from . import views

urlpatterns = [
    path("", views.eventView, name="event"),
    path("staff/", views.staffView, name="staff"),
    path("new", views.createEvent, name="new"),
    path("getEvent/", views.getEvent, name="getEvent"),
]
