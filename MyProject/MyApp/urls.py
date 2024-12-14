from django.urls import path
from . import views

urlpatterns = [
    path('ice-cream/create/', views.create_ice_cream, name='create_ice_cream'),
]
