import datetime
from django.shortcuts import redirect, render

from events.serializers import EventSerializers

from .models import Event

from django.http.response import JsonResponse
from rest_framework import status

from rest_framework.decorators import api_view

# Create your views here.


def staffView(request):
    return render(request, "eventCreate.html")


def eventView(request):
    events = Event.objects.all()
    return render(request, "events.html", {"events": events})


def createEvent(request):
    password = request.POST["password"]
    if password == "yY3mzS^95O2c#^P":
        Event.objects.create(
            event=request.POST["event_text"],
            body=request.POST["body_text"],
            date=request.POST["date_text"],
        )
    return redirect("/events/")


@api_view(["GET"])
def getEvent(request):
    if request.method == "GET":
        events = Event.objects.all()

        def latestChecker(event):
            year, month, day = list(
                map(int, datetime.datetime.now().strftime("%Y %m %d").split())
            )
            if event.date > datetime.date(year=year, month=month, day=day):
                return True

        events = list(filter(latestChecker, events))
        if len(events) != 0:
            event_serializer = EventSerializers(events, many=True)
            return JsonResponse(event_serializer.data, safe=False)
        else:
            return JsonResponse(data=[], status=status.HTTP_200_OK)
