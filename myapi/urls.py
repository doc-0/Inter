
from django.urls import path
from .views import ItemListCreateView, ItemRetrieveUpdateDestroyView ,ImageUrlProcessingView 

urlpatterns = [
    path('list/', ItemListCreateView.as_view(), name='item-list-create'),
    path('create/', ImageUrlProcessingView.as_view(), name='item-list-create'),
    path('list/<int:pk>/', ItemRetrieveUpdateDestroyView.as_view(), name='item-detail'),
]

