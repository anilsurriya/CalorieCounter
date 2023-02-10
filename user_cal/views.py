from django.shortcuts import render, redirect, HttpResponse
from .models import User_cal
from .forms import UserCalForm
# Create your views here.
def user_view(request):
    if not request.user.is_authenticated:
        return redirect('auth_cal:login')
    if not User_cal.objects.filter(user = request.user).exists():
        user_details = User_cal()
        return render(request, 'user.html')
    else:
        user_details = User_cal.objects.get(user = request.user)
        return render(request, 'user.html', {'user_details': user_details})

def updateuser_view(request):
    if not request.user.is_authenticated:
        return redirect('auth_cal:login')
    if not User_cal.objects.filter(user = request.user).exists():
        user_details = User_cal()
    else:
        user_details = User_cal.objects.get(user = request.user)
    if request.method == "POST":
        user_details.user = request.user
        user_details.age = request.POST['age']
        user_details.height = request.POST['height']
        user_details.weight = request.POST['weight']
        user_details.save()
        return HttpResponse("...")
    else:
        user_form = UserCalForm()
        return render(request, 'updateuser.html', {'user_form': user_form})