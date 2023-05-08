#Serializers are similiar to Django Forms
#Serializers covert data input into python object & vice-versa
#Serializers also takes care of validation rules

from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """ Serializes a name field for testing our APIView"""

    #Accept any character input 10 or less char
    name = serializers.CharField(max_length=10)

