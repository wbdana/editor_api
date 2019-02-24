from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from .views import RecordViewSet, UserViewSet

schema_view = get_schema_view(title='Records API')

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'records', RecordViewSet)
router.register(r'users', UserViewSet)