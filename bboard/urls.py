from django.urls import path
from .views import DbCreateView

from .views import index, by_rubric


urlpatterns = [
    path('add/', DbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
]