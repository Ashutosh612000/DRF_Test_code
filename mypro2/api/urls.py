from django.urls import path,include
from api.views import *

urlpatterns = [
    path('student/',StudentAPi.as_view()),
    path('student/<int:pk>/',StudentAPi.as_view())
]