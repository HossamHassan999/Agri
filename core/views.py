from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


class LandPlotAPIView(APIView):
    
    def get(self, request, *args, **kwargs):
        # Fetch all LandPlot objects
        landplots = LandPlot.objects.all()
        
        # Serialize the data
        serializer = LandPlotBookSerializer(landplots, many=True)
        
        return Response(serializer.data,  status=status.HTTP_200_OK)
    
    
    def post(self, request):
        # Deserialize the data
        serializer = LandPlotSerializer(data=request.data)
        if serializer.is_valid():
            
            # Save the new LandPlot object
            
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, *args, **kwargs):
        # Retrieve the object ID from URL kwargs
        landplot_id = kwargs.get('id')
        try:
            landplot = LandPlot.objects.get(id=landplot_id)
        except LandPlot.DoesNotExist:
            return Response({'error': 'LandPlot not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Deserialize the data
        serializer = LandPlotSerializer(landplot, data=request.data, partial=False)
        if serializer.is_valid():
            # Update and save the LandPlot object
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        

        
        
        
        
        
        
        
        
        
