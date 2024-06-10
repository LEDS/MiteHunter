from django.urls import path
from . import views

urlpatterns = [
    path('<int:c_id>', views.main, name=''),
    path('tables/<str:table_name>', views.tables, name='tables')
]