from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import User, Table, Reservation
from .forms import TableForm, ReservationForm

# Басты бет
def home(request):
    return render(request, 'index.html')

# Пайдаланушылар тізімі
def users_list(request):
    users = User.objects.all()
    return render(request, 'users_list.html', {'users': users})

# Белгілі бір пайдаланушының профилі
def user_detail(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, 'user_detail.html', {'user': user})

# Үстелдер тізімі
def tables_list(request):
    tables = Table.objects.all()
    return render(request, 'tables_list.html', {'tables': tables})

# Жаңа үстел қосу
def create_table(request):
    if request.method == "POST":
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tables_list')  # Үстелдер тізіміне қайта бағыттау
    else:
        form = TableForm()
    return render(request, 'create_table.html', {'form': form})

# Бронь жасау
def create_reservation(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tables_list')  # Немесе бронь тізіміне қайта бағыттауға болады
    else:
        form = ReservationForm()
    return render(request, 'create_reservation.html', {'form': form})

# Бронь туралы ақпарат
def reservation_detail(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    return render(request, 'reservation_detail.html', {'reservation': reservation})

# Бронь статусын жаңарту
def update_reservation_status(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    
    if request.method == "POST":
        new_status = request.POST.get("status")
        if new_status:
            reservation.status = new_status
            reservation.save()
            return redirect('reservation_detail', id=reservation.id)
    
    return render(request, 'update_reservation_status.html', {'reservation': reservation})
