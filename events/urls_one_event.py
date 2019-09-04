from django.urls import path, include
from .views import view_one_event, delete_participant, delete_like

urlpatterns = [
    path('<int:pk>', view_one_event, name='view_one_event'),
    path('delete_participant/<int:pk>', delete_participant, name='delete_participant'),
    path('delete_like/<int:pk>', delete_like, name='delete_like'),

]