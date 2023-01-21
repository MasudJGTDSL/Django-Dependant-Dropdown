from django.urls import path
from . import views


app_name = 'Address'

urlpatterns = [
    path('', views.address, name='address'),
    path('get_districts/<int:division_id>', views.get_districts, name='get_districts'),
    path('get_upazilas/<int:district_id>', views.get_upazilas, name='get_upazilas'),
]