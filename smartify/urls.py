from django.urls import path
from .views import List, Data

urlpatterns = [
    path('List/', List.as_view({'get':'list', 'post':'create'})),
    path('Data/<int:id>/', Data.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'}))
]