from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Hotel


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id', 'name', 'num_rooms', 'res_buffer')


# class HotelSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(required=True, allow_blank=False, max_length=100)
#     num_rooms = serializers.IntegerField(required=True, defualt=10)
#     res_buffer = serializers.IntegerField(required=True, defualt=0)
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Hotel` instance, given the validated data.
#         """
#         return Hotel.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Hotel` instance, given the validated data.
#         """
#         instance.name = validated_data.get('name', instance.name)
#         instance.num_rooms = validated_data.get('num_rooms', instance.num_rooms)
#         instance.res_buffer = validated_data.get('res_buffer', instance.res_buffer)
#         instance.save()
#         return instance
