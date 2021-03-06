from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(request, "landing/landing.html")

def overview(request):
    return render(request, "landing/overview.html")