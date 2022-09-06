from django.urls import path, include
from apps.books.router import router

urlpatterns = [
    path('api/', include(router.urls)),
]

