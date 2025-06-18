from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
# from .serializers import CitySerializer
from rest_framework.decorators import action
import requests

class weatherView(viewsets.ViewSet):  
            
# --------------------End points to get the weather information of the country information with putting the name of the country--------------               
        @action(detail=False, methods=['GET'], url_path='get_weather')
        def get_weather(self, request):
            user_city = request.query_params.get('q', None)
            
            if not user_city:
                return Response({"Error:" "You're messing one information, example of what you need to put in the url at the end(?q=INFO) "}, status=status.HTTP_400_BAD_REQUEST)               
             
            url = f"http://api.weatherapi.com/v1/current.json?key=bdedcc2092b24167a9e164011251806&q={user_city}&aqi=no"
            response = requests.get(url)
            data = response.json()
            return Response(data)
        
       
        
    
# --------------------End point to get a place putting the name--------------                
        @action(detail=False, methods=['GET'], url_path='get_place')
        def get_place(self, request):
            user_city = request.query_params.get('q', None)
            if not user_city:
                   return Response({"Error: " "You're messing one information, example of what you need to put in the url at the end(?q=INFO) "}, status=status.HTTP_400_BAD_REQUEST)           
            
            url = f"http://api.weatherapi.com/v1/timezone.json?key=bdedcc2092b24167a9e164011251806&q={user_city}"
            response = requests.get(url)
            data = response.json()
            return Response(data)




# --------------------End point for the neaarest place between two differents latitud and longitud--------------        
        @action(detail=False, methods=['GET'], url_path='get_astronomy')
        def get_astronomy(self, request):
            user_city = request.query_params.get('q', None)
            
            if not user_city:
                  return Response({"Error:" "You're messing one information, example of what you need to put in the url at the end(?q=INFO) "}, status=status.HTTP_400_BAD_REQUEST)        
            
            url = f" http://api.weatherapi.com/v1/astronomy.json?key=bdedcc2092b24167a9e164011251806&q={user_city}&dt=2025-06-18 "
            response = requests.get(url)
            data = response.json()
            return Response(data)
        