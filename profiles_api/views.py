# Import APIView class from rest_framework.views module
# Import Response object
# The rest_framework is specified in our requirements.txt file
from rest_framework.views import APIView
from rest_framework.response import Response
# status object is a list of handy HTTP status codes used when return
#responses from API
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    """ Test API View"""
    """ Creating a new class based on the APIView class"""
    # Allow us to define application logic for our endpoint(url)
    # we will assign to this view

    #When sending post,put,patch request -> expect an input with name
    serializer_class= serializers.HelloSerializer

# request object -> passed in by the djangorest framework. Contains details of the request being made to the API
    def get(self,request, format=None):
        """Returns a list of APIView features"""

        # These are all the functions that can add to API view to support
        #Different http requests
        an_apiview =[
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        #Every function added to APIview must return a response object
        #Response needs to contain either dictionary or list which will output
        # Converts response object into a JSON
        return Response({'message': 'Hello', 'an_apiview': an_apiview})
    
    def post(self,request):
        """Create a hello message with our name"""

        #self.serializer_class -> retrives configured serializer class for our view
        # When making a POST request, data gets passed in as  a request. data 
        serializer = self.serializer_class(data=request.data)

        # Only return if input is valid -> need to create condition 
        # where input is not valid

        #is_valid() class -> way to check validation
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({'message':message})
        
        else:
            #By default -> response return HTTP 200 OK request
            # Since eroor message-> need to change code (FYI -> CAN  just pass the number 400)
            # But better to specify
            return Response(serializer.errors, 
                            status= status.HTTP_400_BAD_REQUEST)
        
    # UsED TO update objects
    #pk -. primary key -> takes in ID of object to be updated with put request
    def put(self,request,pk=None):
        """Handle Updating an object ,Put REQUESTs"""
        return Response({'method': 'PUT'})
    
    #Patch request -> only update fields that were provided in the request
    def patch(self,request,pk=None):
        """Handle partial update of object, PATCH request"""
        return Response({'method': 'PATCH'})
    
    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})


