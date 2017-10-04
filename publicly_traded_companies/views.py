from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter

from publicly_traded_companies.models import Exchange, Company
from publicly_traded_companies.serializers import ExchangeSerializer, CompanySerializer


class StandardLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100


class ExchangesView(ListAPIView):
    queryset = Exchange.objects.all().order_by('name')
    serializer_class = ExchangeSerializer
    pagination_class = StandardLimitOffsetPagination
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'nickname')


class ExchangeView(RetrieveAPIView):
    queryset = Exchange.objects.all()
    serializer_class = ExchangeSerializer


class CompaniesView(ListAPIView):
    queryset = Company.objects.all().order_by('name')
    serializer_class = CompanySerializer
    pagination_class = StandardLimitOffsetPagination
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'ticker')


class CompanyView(RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
