from django.conf import settings
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from classnowapp.models.user_est import User_est
from classnowapp.serializers.user_est_serializer import User_est_serializer

class userDetailView(generics.RetrieveAPIView):
    queryset = User_est.objects.all()
    serializer_class = User_est_serializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        return super().get(request, *args, **kwargs)