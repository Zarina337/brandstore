from django.urls import path 
from .views import  manepage_view ,cotegory_view
app_name = 'main'
urlpatterns = [
    path( '' ,  manepage_view , name='home'),
    path( 'cotegory/' ,  cotegory_view , name='cotegory')
]
