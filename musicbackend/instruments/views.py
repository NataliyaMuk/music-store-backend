from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Blog, Img_for_instrument, Instruments, Subcategory
from .serializers import (
    BlogSerializer,
    Img_for_instrumentSerializer,
    InstrumentsSerializer, SubcategorySerializer,
)


class InstrumentsPagination(PageNumberPagination):
    page_size = 9


class InstrumentsViewSet(viewsets.ModelViewSet):
    serializer_class = InstrumentsSerializer
    pagination_class = InstrumentsPagination

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if not pk:
            return Instruments.objects.all()
        return Instruments.objects.filter(pk=pk)

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category", "subcategory"]


class SubCatViewSet(viewsets.ModelViewSet):
    serializer_class = SubcategorySerializer
    queryset = Subcategory.objects.all()

    def get_queryset(self):
        sub_id = self.request.query_params.get('id')
        return Subcategory.objects.filter(category_id=sub_id)


class ImagesViewSet(viewsets.ModelViewSet):
    serializer_class = Img_for_instrumentSerializer
    queryset = Img_for_instrument.objects.all()

    def get_queryset(self):
        ins_id = self.request.query_params.get('id')
        return Img_for_instrument.objects.filter(instrument_id=ins_id)


class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if not pk:
            return Blog.objects.all()
        return Blog.objects.filter(pk=pk)
