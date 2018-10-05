from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class HealthChk(APIView):
    def get(self, request):
        data = {
            "message": "Welcome to Kliento API",
            "method": str(request.method.lower())
        }
        return Response(data=data, status=status.HTTP_200_OK)


class V1HealthChk(APIView):
    def get(self, request):
        data = {
            "message": "Welcome to Kliento V1 API",
            "method": str(request.method.lower())
        }
        return Response(data=data, status=status.HTTP_200_OK)