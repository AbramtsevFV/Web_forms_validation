from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import *

urlpatterns = [
            path('template/', csrf_exempt(Templates_views.as_view()), name='template'),
]