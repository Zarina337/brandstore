from django.shortcuts import render

# Create your views here.
def manepage_view(request):

    return render(request , 'main.html')