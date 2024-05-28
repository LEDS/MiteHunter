from django.urls import path
from . import views

urlpatterns = [
    path('<int:c_id>', views.main, name=''),
    path('imagens/<int:c_id>', views.send_images_page, name='send_images')
]