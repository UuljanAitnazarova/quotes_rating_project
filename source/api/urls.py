from django.urls import path, include
from rest_framework import routers
from api.views import QuoteViewSet, IncreaseRating, DecreaseRating

router = routers.DefaultRouter()
router.register(r'quotes', QuoteViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('quotes/<int:pk>/increase/', IncreaseRating.as_view()),
    path('quotes/<int:pk>/decrease/', DecreaseRating.as_view()),
]