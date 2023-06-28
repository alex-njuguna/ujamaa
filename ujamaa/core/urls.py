from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('settings/', settings, name='settings'),

    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', logout, name='logout'),
]