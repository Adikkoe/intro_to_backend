from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Reservation
from django.contrib.auth.models import User
from tables.models import Table
import json

@csrf_exempt
def create_reservation(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = User.objects.get(pk=data["user_id"])
        table = Table.objects.get(pk=data["table_id"])

        # Тексеру: сол күні басқа бронь бар ма?
        existing_reservation = Reservation.objects.filter(user=user, date=data["date"]).exists()
        if existing_reservation:
            return JsonResponse({"error": "You already have a reservation on this date"}, status=400)

        reservation = Reservation.objects.create(user=user, table=table, date=data["date"])
        return JsonResponse({"id": reservation.id, "user": reservation.user.username, "table": reservation.table.number, "date": str(reservation.date), "status": reservation.status})

def reservation_detail(request, id):
    reservation = get_object_or_404(Reservation, pk=id)
    return JsonResponse({"id": reservation.id, "user": reservation.user.username, "table": reservation.table.number, "date": str(reservation.date), "status": reservation.status})

@csrf_exempt
def update_reservation_status(request, id):
    reservation = get_object_or_404(Reservation, pk=id)
    data = json.loads(request.body)
    reservation.status = data["status"]
    reservation.save()
    return JsonResponse({"message": "Reservation status updated"})
