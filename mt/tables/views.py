from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Table
import json

@csrf_exempt
def create_table(request):
    if request.method == "POST":
        data = json.loads(request.body)
        table = Table.objects.create(number=data["number"], seats=data["seats"])
        return JsonResponse({"id": table.id, "number": table.number, "seats": table.seats, "is_available": table.is_available})

def tables_list(request):
    tables = list(Table.objects.values())
    return JsonResponse(tables, safe=False)
