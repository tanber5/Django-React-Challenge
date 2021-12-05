from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    id = serializers.CharField()

class DataSerializer(serializers.Serializer):
    errors = serializers.CharField(required=False)
    value = UserSerializer(required=False)
