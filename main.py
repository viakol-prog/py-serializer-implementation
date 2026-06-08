import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from serializers import CarSerializer
from car.models import Car


def serialize_car_object(car: Car) -> bytes:
    """Accepts a Car instance and returns a JSON string (bytes) with its data."""
    serializer = CarSerializer(car)
    json_bytes = JSONRenderer().render(serializer.data)
    return json_bytes


def deserialize_car_object(json_data: bytes) -> Car:
    """Accepts a JSON string (bytes), validates it, and returns a Car instance."""
    stream = io.BytesIO(json_data)
    data = JSONParser().parse(stream)

    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)

    car_instance = serializer.save()
    return car_instance
