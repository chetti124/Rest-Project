from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    # authentication_classes = [BasicAuthentication]
    # authentication_classes = [SessionAuthentication]
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["get"], url_path='inactive-prod',url_name='inactive_prod')
    def get_incative_data(self, request):
        queryset = Product.objects.filter(is_active=0)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=["post"], url_path='restore-stud/(?P<pk>[^/.]+)',url_name='restore_prod')
    def restore_data(self, request, pk=None):
        data = Product.objects.get(pk=pk)
        data.is_active = True
        data.save()
        return Response("data restored sucessfully")

