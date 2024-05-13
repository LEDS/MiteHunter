from django.urls import path
from . import views

urlpatterns = [
    path('<int:c_id>', views.main, name=''),
]