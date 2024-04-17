from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name=''),
    path('export_data/', views.export_data, name='export_data'),
]