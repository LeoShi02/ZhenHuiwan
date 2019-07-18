from django.shortcuts import render


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def codes(request):
    return render(request, 'codes.html')


def gallery(request):
    return render(request, 'gallery.html')


def icons(request):
    return render(request, 'icons.html')


def index(request):
    return render(request, 'index.html')


def services(request):
    return render(request, 'services.html')


def single(request):
    return render(request, 'single.html')
