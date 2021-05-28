from django.urls import path, include
from rest_framework import routers
from api.views import QuoteViewSet

router = routers.DefaultRouter()
router.register(r'quotes', QuoteViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
]