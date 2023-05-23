from .models import *
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import InstrumentsSerializer, BlogSerializer, Img_for_instrumentSerializer
from rest_framework.decorators import action

class InstrumentsPagination(PageNumberPagination):
    page_size = 6

class InstrumentsViewSet(viewsets.ModelViewSet):
    serializer_class = InstrumentsSerializer
    pagination_class = InstrumentsPagination

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if not pk:
            return Instruments.objects.all()
        return Instruments.objects.filter(pk=pk)
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']

    
    
class ImagesViewSet(viewsets.ModelViewSet):
    serializer_class = Img_for_instrumentSerializer
    images = Img_for_instrument.objects.select_related().filter(instrument_id=6)

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if not pk:
            return Img_for_instrument.objects.all()
        return Img_for_instrument.objects.filter(pk=pk)


class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if not pk:
            return Blog.objects.all()
        return Blog.objects.filter(pk=pk)
