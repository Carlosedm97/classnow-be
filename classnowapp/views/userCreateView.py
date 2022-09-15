from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from classnowapp.serializers.user_est_serializer import User_est_serializer

class userCreateView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = User_est_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData = {
            "username_est": request.data["username_est"],
            "password": request.data["password"]
        }

        tokenSerializer = TokenObtainPairSerializer(data=tokenData)

        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)