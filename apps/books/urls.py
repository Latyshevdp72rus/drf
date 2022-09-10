from django.urls import path, include
from apps.books.router import router

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
