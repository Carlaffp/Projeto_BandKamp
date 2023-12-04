from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from rest_framework.pagination import PageNumberPagination
from .serializers import SongSerializer
from albums.models import Album
from rest_framework.generics import ListCreateAPIView


class SongView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    

    def perform_create(self, serializer):
        found_album = get_object_or_404(Album, pk=self.kwargs.get("pk"))
        return serializer.save(album=found_album)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        queryset = Song.objects.filter(album_id=id)
        return queryset

