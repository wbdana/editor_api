from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Owner, Collaborator, Reader, Record
from .serializers import UserSerializer, OwnerSerializer, CollaboratorSerializer, ReaderSerializer, RecordSerializer
from .permissions import IsRecordOwnerOrReadOnly
from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.reverse import reverse
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'records': reverse('record-list', request=request, format=format),
    })


@api_view(['POST'])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)
    if not user:
        return Response({
            "error": "Login failed",
        }, status=HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key})


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class CollaboratorViewSet(viewsets.ModelViewSet):
    queryset = Collaborator.objects.all()
    serializer_class = CollaboratorSerializer


class ReaderViewSet(viewsets.ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsRecordOwnerOrReadOnly,
    )

    # @action(detail=True, methods=["GET", "POST"])
