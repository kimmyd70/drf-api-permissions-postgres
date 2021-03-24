from rest_framework import generics
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Woman
# from .permissions import IsAuthorOrReadOnly
from .serializers import WomanSerializer


class WomanList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer


class WomanDetail(generics.RetrieveDestroyAPIView):
    # permission_classes = (IsAuthorOrReadOnly,)
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer
