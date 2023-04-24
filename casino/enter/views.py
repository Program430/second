from django.shortcuts import render
from main import views as large
from .models import User
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

def enter_enter(request):
    if request.POST:
        login = request.POST.get("login")
        password = request.POST.get("password")
        user = User.objects.filter(login=login)
        error = {"error": "Login or password is wrong!"}

        if user.exists():
            user = User.objects.filter(login=login, password=password)
            if user.exists():
                return large.main_page(request)
            else:
                return render(request, "enter_enter.html", context=error)
        else:
            return render(request, "enter_enter.html", context=error)
    else:
        return render(request, "enter_enter.html")


def enter_register(request):
    return render(request, "enter_register.html")

