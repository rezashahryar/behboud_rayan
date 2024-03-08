from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from hamayesh.models import Hamayesh, ParticipantHamayesh
from .serializers import HamayeshSerializer, ParticipantsSerializer
from rest_framework import generics


class RegisterHamayesh(generics.ListCreateAPIView):
    queryset = ParticipantHamayesh.objects.all()
    serializer_class = ParticipantsSerializer


# @api_view(['POST'])
# def hamayesh_register(request):
#     if request.method == 'POST':
#         serializer = ParticipantsSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response('ok')


class HamayeshViewSet(ModelViewSet):
    queryset = Hamayesh.objects.prefetch_related('participants').all()
    serializer_class = HamayeshSerializer

