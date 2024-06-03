from django.urls import path
from . import views

urlpatterns = [
    path('<int:c_id>', views.main, name=''),
    path('<str:table_name>', views.table_page, name='table_page'),
    path('imagens/<int:c_id>', views.send_images_page, name='send_images')
]