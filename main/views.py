from django.shortcuts import render

# Create your views here.
def manepage_view(request):

    return render(request , 'main.html')

def cotegory_view(request):

    return render(request , 'cotegory.html')

def detail_view(request):
    return render(request, 'detail.html')


def cart_view(request):
    return render(request, 'mycart.html')