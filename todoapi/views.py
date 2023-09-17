from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Todo
from .serializers import TodoSerializer

# Create your views here.
@api_view(['GET'])
def test(request):
    return Response({'Success':'Tested successfully'})


# @api_view(['GET'])
# def get_all_todo(request):
#     todo = Todo.objects.all()
#     serializer = TodoSerializer(todo, many=True)
#     return Response(serializer.data, status=200)

# @api_view(['POST'])
# def post_todo(request):
#     serializer = TodoSerializer(data= request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data,status=200)
#     return Response(serializer.errors,status = 400)

@api_view(['GET','POST'])
def all_todo(request):
    if request.method == 'GET':
        todo = Todo.objects.all()
        serializer = TodoSerializer(todo,many=True)
        return Response(serializer.data,status = 200)
    elif request.method == 'POST':
        serializer = TodoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 200)
        return Response(serializer.errors, status = 400)
    
@api_view(['GET','PUT','DELETE'])
def todo_maipulate(request,id):
    try:
        todo = Todo.objects.get(id = id)
    except Todo.DoesNotExist:
        return Response({'Error':'Todo not found'},status = 404)
    
    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return Response(serializer.data,status=200)
    elif request.method == 'PUT':
        serializer = TodoSerializer(todo , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status= 400)
    elif request.method == 'DELETE':
        todo.delete()
        return Response({'Success':'Todo deleted successfully'},status = 200)
    