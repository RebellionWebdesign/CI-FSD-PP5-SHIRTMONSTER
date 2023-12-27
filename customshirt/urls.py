from django.urls import path
from .views import CustomShirtView


urlpatterns = [
    path('custom_shirts/', CustomShirtView.as_view(), name='custom_shirts'),
]
