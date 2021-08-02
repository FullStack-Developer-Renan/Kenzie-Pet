from django.urls import path
from .views import AnimalDetailView, AnimalView

urlpatterns = [
    path('animals/', AnimalView.as_view()),
    path('animals/<int:animal_id>/', AnimalDetailView.as_view())
]