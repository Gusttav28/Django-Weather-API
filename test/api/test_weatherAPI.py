import pytest
from rest_framework.test import APIClient

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db 
@pytest.mark.parametrize("api_call", ["caracas", "valencia", "barcelona"])
def test_get_weather(api_client, api_call):
    city = api_call
    response = api_client.get(f"/api/weather/get_place/?q={city}")
    
    assert response.status_code == 200
    
    data = response.json()
    assert data["location"]["name"].lower() == city.lower()
    
        
@pytest.mark.django_db 
@pytest.mark.parametrize("api_call", ["caracas", "valencia", "barcelona"])
def test_get_place(api_client, api_call):
    city = api_call
    
    response = api_client.get(f"/api/weather/get_weather/?q={city}")
    assert response.status_code == 200
    
    data = response.json()   
    assert data["location"]["name"].lower() == city.lower()
    
    
@pytest.mark.django_db

@pytest.mark.parametrize("api_call", ["caracas", "valencia", "barcelona"])
def test_get_astronomy(api_client, api_call):
    city = api_call
    response = api_client.get(f"/api/weather/get_astronomy/?q={city}")
    data = response.json()   
    assert data["location"]["name"].lower() == city.lower()