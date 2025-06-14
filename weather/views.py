from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
# from .serializers import CitySerializer
from rest_framework.decorators import action
import requests

class weatherView(viewsets.ViewSet):  
            
# --------------------End points to get the weather information either with the name of the place or with the latitud and the longitud--------------               
        @action(detail=False, methods=['GET'], url_path='get_weather')
        def get_weather(self, request):
            user_city = request.query_params.get('place_id', None)
            
            if not user_city:
                return Response({"Error:" "You're messing one information, example(place_id=INFO"}, status=status.HTTP_400_BAD_REQUEST)                 
            url = f"https://www.meteosource.com/api/v1/free/point?place_id={user_city}&sections=current%2C%20hourly&timezone=auto&language=en&units=auto&key=lvetw31pfazam0dvgan3k4u9p5qu7u89wf17xgvb"
            response = requests.get(url)
            data = response.json()
            return Response(data)
        
        @action(detail=False, methods=['GET'], url_path='get_weather2')
        def get_weather2(self, request):
            user_lat = request.query_params.get('lat', None)
            user_lon = request.query_params.get('lon', None) 
            
            if not user_lat and user_lon:
                return Response({"Error:" "You're messing one information, example(lat = number and lon = number"}, status=status.HTTP_400_BAD_REQUEST)                 
            url = f"https://www.meteosource.com/api/v1/free/point?lat={user_lat}&lon={user_lon}&sections=current%2C%20hourly&timezone=auto&language=en&units=auto&key=lvetw31pfazam0dvgan3k4u9p5qu7u89wf17xgvb"
            response = requests.get(url)
            data = response.json()
            return Response(data)
        
        
        

# --------------------End point to get a place putting the name or the zip code--------------                
        @action(detail=False, methods=['GET'], url_path='get_place')
        def get_place(self, request):
            user_city = request.query_params.get('place_id', None)
            if not user_city:
                return Response({"Error:" "You're messing one information, example(place_id=INFO"}, status=status.HTTP_400_BAD_REQUEST)
            url = f"https://www.meteosource.com/api/v1/free/find_places?text={user_city}&language=en&key=lvetw31pfazam0dvgan3k4u9p5qu7u89wf17xgvb"
            response = requests.get(url)
            data = response.json()
            return Response(data)


# --------------------End point for the neaarest place between two differents latitud and longitud--------------        
        @action(detail=False, methods=['GET'], url_path='nearest_place')
        def nearest_place(self, request):
            user_lat = request.query_params.get('lat', None)
            user_lon = request.query_params.get('lon', None) 
            if not user_lat and user_lon:
                return Response({"Error":"You're messing two information, example (lat = Numbers, lon = numbers)"}, status=status.HTTP_400_BAD_REQUEST)

            url = f"https://www.meteosource.com/api/v1/free/nearest_place?lat={user_lat}&lon={user_lon}&language=en&key=lvetw31pfazam0dvgan3k4u9p5qu7u89wf17xgvb"
            
            response = requests.get(url)
            data = response.json()
            return Response(data)