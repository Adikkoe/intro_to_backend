from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def users_list(request):
    if request.method == "GET":
        users = list(User.objects.values("id", "username", "email"))
        return JsonResponse(users, safe=False)

    elif request.method == "POST":
        data = json.loads(request.body)
        user = User.objects.create_user(username=data["username"], email=data["email"], password=data["password"])
        return JsonResponse({"id": user.id, "username": user.username, "email": user.email})
    
def user_detail(request, id):
    user = get_object_or_404(User, pk=id)
    return JsonResponse({"id": user.id, "username": user.username, "email": user.email})
