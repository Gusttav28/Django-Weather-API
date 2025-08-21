# Django-Weather-API

Django-Weather-API is a RESTful backend service built with Django REST Framework (DRF) that provides real-time weather data through a custom API. This backend serves as the core of a full-stack application, which includes multiple frontend implementations—such as a vanilla JavaScript app and a React + Next.js version. The main purpose of this project is to strengthen backend development skills while ensuring clean API design and proper data handling for frontend integration.

## 🚀 Project Purpose

This backend project was created as a foundation for experimenting with different frontend stacks. By building and maintaining a custom API, the goal is to practice core backend concepts like serialization, routing, and API responses, while supporting multiple user interfaces.

## 🌐 Frontend Repositories

You can view the frontend implementations that consume this API here:

👉 WeatherJS - Vanilla JavaScript Frontend[https://github.com/Gusttav28/WeatherJS]

To test this API in action, visit the live deployed frontend:

👉 Live Weather App[weather-bygus.vercel.app
+2]

## 🧩 Features

RESTful API design following Django REST Framework standards.

Endpoints to fetch weather information such as temperature, humidity, and Astronomy.

Clean and modular structure for easy integration with multiple frontend clients.

CORS enabled to allow requests from external web applications.

Scalable and extensible setup for future data sources or external APIs.

## 🛠 Technologies Used

Backend: Python, Django, Django REST Framework

Environment: SQLite (for development)

Other: Django CORS Headers, requests module (if consuming third-party APIs)

## ▶️ How to Run This Project

Clone the repository

git clone https://github.com/your-user/django-weather-api.git
cd django-weather-api


Create a virtual environment and activate it

python -m venv env
source env/bin/activate  # For Windows: env\Scripts\activate

Install dependencies

pip install -r requirements.txt

Run migrations and start the server

python manage.py migrate
python manage.py runserver

The API will be available at http://localhost:8000.

## 🔌 Main Endpoints

GET /api/get_weather/ – Returns the current weather data.

GET /api/get_place/ – Returns weather data for a specific city.

GET /api/get_astronomy/ – Returns the astronomy data for a specific country.

(Optional) POST or PUT endpoints depending on project scope.

## 🧪 Future Improvements

Add token-based authentication (e.g., JWT).

Implement caching to reduce external API calls.

Integrate background tasks using Celery for scheduled updates.

Expand API to include forecast and historical data.

# 👨‍💻 About Me

If you want to learn more about my work or get in touch, you can find me here:

🌐 Website: gustavocamacho.dev[https://www.gustavocamacho.net/]

💼 LinkedIn: Gustavo Camacho[https://www.linkedin.com/in/gustavo-camacho-b9a64b243/]
