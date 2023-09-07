from django.urls import path
from .views import AllView, CreateSensor, UpdateSensor, CreateMeasurement, SensorView

app_name = 'measurement'

urlpatterns = [
    path('view_all/', AllView.as_view()),
    path('change_sensor/<pk>/', UpdateSensor.as_view()),
    path('add_sensor/', CreateSensor.as_view()),
    path('add_measurement/', CreateMeasurement.as_view()),
    path('view_sensor/<pk>', SensorView.as_view()),

]
