# Import APIView class from rest_framework.views module
# Import Response object
# The rest_framework is specified in our requirements.txt file
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """ Test API View"""
    """ Creating a new class based on the APIView class"""
    # Allow us to define application logic for our endpoint(url)
    # we will assign to this view

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

