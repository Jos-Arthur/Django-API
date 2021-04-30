from rest_framework import serializers
from api_stage.models import (Users, UserProfiles, Posts, Files, Comments)
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('username',
                  'email',
                  'password')
        extra_kwargs = {'password': {'write_only': True}}


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfiles
        fields = (
            'first_name',
            'last_name',
            'date_birth',
            'gender',
            'profession',
            'phone',
            'user')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('id',
                  'mots_recherche',
                  'social_media',
                  'type_document',
                  'comment',
                  'user')


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = ('id',
                  'type_file',
                  'file_name',
                  'comment',
                  'user')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id',
                  'title',
                  'comment',
                  'user')
