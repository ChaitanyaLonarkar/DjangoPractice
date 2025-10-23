from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import TodoItemSerializer
from .models import TodoItem

# Create your views here.
class TodoCreateListView(APIView):
    def get(self, request):
        todos = TodoItem.objects.all()
        serializer = TodoItemSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoCrudView(APIView):
    def get(self, request, pk):
        todos = TodoItem.objects.get(pk=pk)
        print(todos,'todosfdgdfgdfgcvb')
        serializer = TodoItemSerializer(todos)
        return Response(serializer.data)


    def put(self, request, pk):
        todo = TodoItem.objects.get(pk=pk)
        serializer = TodoItemSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        todo = TodoItem.objects.get(pk=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


    
