from django.http import HttpResponse
from django.shortcuts import render

def show_test(request):
    return HttpResponse('test')
def index(request):
    return render(request, 'index.html')
def image_page(request):
    return render(request, 'data/images.html')
def infrared_page(request):
    return render(request, 'data/infrared.html')
def ultrasonic_page(request):
    return render(request, 'data/ultrasonic.html')
def head(request):
    return render(request, 'head.html')
def left(request):
    return render(request, 'left.html')
def main(request):
    return render(request, 'main.html')
def foot(request):
    return render(request, 'foot.html')
def js(request):
    return render(request, 'js.html')