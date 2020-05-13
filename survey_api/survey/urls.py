from django.urls import path, include
from rest_framework import routers
from .views import PollsViewSet

router = routers.DefaultRouter()

router.register(r'polls', PollsViewSet)

urlpatterns = [
    path('', include(router.urls))
]
