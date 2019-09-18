from django.urls import path, include
from .views import view_one_event, delete_participant, delete_like, delete_event, edit_event

urlpatterns = [
    path('<int:pk>', view_one_event, name='view_one_event'),
    path('delete_participant/<int:pk>', delete_participant, name='delete_participant'),
    path('delete_like/<int:pk>', delete_like, name='delete_like'),
    path('delete_event/<int:pk>', delete_event, name='delete_event'),
    path('edit_event/<int:pk>', edit_event, name='edit_event')
]