from rest_framework import serializers
from .models import Role
class RoleSerializer(serializers.Serializer):
    role_name=serializers.CharField(max_length=100)
    status=serializers.IntegerField()
    created_at=serializers.DateTimeField()
    updated_at=serializers.DateTimeField()

    def create(self,validated_data):
     return Role.objects.create(**validated_data)