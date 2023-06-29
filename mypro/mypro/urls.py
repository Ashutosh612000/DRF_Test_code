
from django.contrib import admin
from django.urls import path,include 
from api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('stuinfo/<int:pk>',views.student_get),
    # path('stuinfo/', views.student_create),
    path('user/',views.user_get)
]
