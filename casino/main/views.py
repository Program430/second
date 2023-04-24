from django.shortcuts import render


def dop_function(request):
    name = request.POST.get("firstname")
    lastname = request.POST.get("lastname")
    b = True

    if name != "1":
        b = False
    if lastname != "1":
        b = False

    if b:
        a = render(request, 'Success.html')
    else:
        a = render(request, 'error.html')
    return a


def main_page(request):
    return render(request, 'home.html')