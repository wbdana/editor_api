from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from .views import RecordViewSet, UserViewSet, OwnerViewSet, CollaboratorViewSet, ReaderViewSet

schema_view = get_schema_view(title='Records API')

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'records', RecordViewSet)
router.register(r'users', UserViewSet)
router.register(r'owners', OwnerViewSet)
router.register(r'collaborators', CollaboratorViewSet)
router.register(r'readers', ReaderViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('schema/', schema_view),
    path('', include(router.urls)),
]
