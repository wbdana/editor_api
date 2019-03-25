from rest_framework import serializers
from .models import Owner, Collaborator, Reader, Record
from django.contrib.auth.models import User


class RecordSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(many=False, view_name='owner-detail', read_only=True)

    class Meta:
        model = Record
        fields = (
            'url',
            'id',
            'created',
            'name',
            'extension',
            'path',
            'content',
            'owner',
            'collaborators',
            'readers',
        )
        depth = 2

    def create(self, validated_data):
        record = Record.objects.create(**validated_data)
        return record


class UserSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(many=False, view_name='owner-detail', read_only=True)
    collaborator = serializers.HyperlinkedRelatedField(many=False, view_name='collaborator-detail', read_only=True)
    reader = serializers.HyperlinkedRelatedField(many=False, view_name='reader-detail', read_only=True)

    class Meta:
        model = User
        fields = (
            'url',
            'id',
            'username',
            'owner',
            'collaborator',
            'reader',
        )


class OwnerSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    records = RecordSerializer(many=True, read_only=True)

    class Meta:
        model = Owner
        fields = (
            'url',
            'id',
            'user',
            'records',
        )


class CollaboratorSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    records = RecordSerializer(many=True, read_only=True)

    class Meta:
        model = Collaborator
        fields = (
            'url',
            'id',
            'user',
            'records',
        )


class ReaderSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    records = RecordSerializer(many=True, read_only=True)

    class Meta:
        model = Reader
        fields = (
            'url',
            'id',
            'user',
            'records',
        )
