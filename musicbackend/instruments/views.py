from .models import *
from rest_framework import viewsets
from .serializers import InstrumentsSerializer
from rest_framework.pagination import PageNumberPagination

class InstrumentsPagination(PageNumberPagination):
    page_size = 5

class InstrumentsViewSet(viewsets.ModelViewSet):
    serializer_class = InstrumentsSerializer
    pagination_class = InstrumentsPagination

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if not pk:
            return Instruments.objects.all()
        return Instruments.objects.filter(pk=pk)
