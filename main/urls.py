from django.urls import path 
from .views import  manepage_view ,cotegory_view, detail_view, cart_view
app_name = 'main'
urlpatterns = [
    path( '' ,  manepage_view , name='home'),
    path( 'cotegory/' ,  cotegory_view , name='cotegory'),
    path('detail/', detail_view, name='detail'),
    path('cart/', cart_view, name='cart')
]
