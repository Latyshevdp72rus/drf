from django.urls import path, include
from apps.books.views import PublishingHouseAPIView, PublishingHoueseCreateAPIView, AuthorAPIView, AuthorCreateAPIView,BookAPIView,BookCreateAPIView

urlpatterns = [
    path('publishing_house/<int:pk>', PublishingHouseAPIView.as_view(), ),
    path('publishing_house', PublishingHoueseCreateAPIView.as_view(), ),
    path('Author/<int:pk>', AuthorAPIView.as_view(), ),
    path('Author', AuthorCreateAPIView.as_view(), ),
    path('Book/<int:pk>', BookAPIView.as_view(), ),
    path('Book', BookCreateAPIView.as_view(), ),

]
