from pet_app.models import Animal, Characterist, Group
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AnimalSerializer
from rest_framework import status

    
class AnimalView(APIView):
    def get(self, request):    
        animals = Animal.objects.all()
        
        serialized = AnimalSerializer(animals, many=True)
        return Response(serialized.data)
    
    def post(self, request):
        serializer = AnimalSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        validated_data = serializer.validated_data
          
        group  = validated_data.pop('group')
        
        group = Group.objects.get_or_create(**group)[0]

        characteristics = validated_data.pop('characteristics')
        
        animal = Animal.objects.create(**validated_data, group=group)

        char_list = []

        for characteristic in characteristics:
            characteristic = Characterist.objects.get_or_create(**characteristic)[0]
            char_list.append(characteristic)
        
        animal.characteristics.set(char_list)
           
        serializer = AnimalSerializer(animal)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class AnimalDetailView(APIView):
    def get(self, request, animal_id=''):
        animal = get_object_or_404(Animal, id=animal_id)
        serializer = AnimalSerializer(animal)
        return Response(serializer.data)
          
    def delete(self, request, animal_id):
        animal = get_object_or_404(Animal, id=animal_id)
        
        animal.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
    