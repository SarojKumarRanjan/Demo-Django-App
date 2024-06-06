from django.shortcuts import render

# Create your views here.
def demoapp(request):
    return render(request, 'demoapp/all_demo.html')
