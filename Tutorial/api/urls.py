from .views import *
from django.urls import path,include
from rest_framework.routers import SimpleRouter,DefaultRouter

router = DefaultRouter()
router.register('quest',QuestionViewSet)

urlpatterns = [
    path('v2/',include(router.urls)),
    path('q/',ReplyView.as_view()),
    path('v/<pk>/',ReplyMix.as_view())
]
