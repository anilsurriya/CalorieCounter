from django.urls import path
from . import views

app_name = 'user_cal'

urlpatterns = [
    path('user', views.user_view, name='userview'),
    path('updateuser', views.updateuser_view, name='updateuser')
]
