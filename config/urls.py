from django.urls import path
from django.views.generic import View
from config.views import *


urlpatterns = [
path('', Home.as_view(), name='home'),
]