
from rest_framework import serializers
from .models import TodoItem


class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        # fields = ["url", "username", "email", "groups"]
        fields="__all__"

class TodoCrudSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ["id", "title", "description", "completed",]
        # fields="__all__"