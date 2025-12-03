from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import TeacherViewSet,StudentViewSet,PriceViewSet


router = DefaultRouter()
router.register('teacher',TeacherViewSet)
router.register('stedent',StudentViewSet)
router.register('Price',PriceViewSet)

urlpatterns = [
    path("",include(router.urls))
]