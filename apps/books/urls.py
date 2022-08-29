from django.urls import path, include
from apps.books.views import PublishHouseAction

    # PubViewDetail,PublishingHouseAction

urlpatterns = [
    path('publishing_house/', PublishHouseAction.as_view()),

    # path('publishing_house/', PublishingHouseAction.as_view(),
    # path('publishing_house/<int:pk>', PubViewDetail.as_view())),
]

    # PublishingHouseAction
# PublishingHoueseCreateAPIView, AuthorAPIView, AuthorCreateAPIView,BookAPIView,BookCreateAPIView
    # path('publishing_house/', PublishingHouseAction.as_view(), ),
    # path('publishing_house', PublishingHoueseCreateAPIView.as_view(), ),
    # path('Author/<int:pk>', AuthorAPIView.as_view(), ),
    # path('Author', AuthorCreateAPIView.as_view(), ),
    # path('Book/<int:pk>', BookAPIView.as_view(), ),
    # path('Book', BookCreateAPIView.as_view(), ),

