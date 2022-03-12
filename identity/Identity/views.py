from rest_framework import status, response
from rest_framework.views import APIView


class Heartbeat(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        return response.Response(data={"status": True, "message": "OK"}, status=status.HTTP_200_OK)
