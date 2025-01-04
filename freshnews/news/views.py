from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.forms import model_to_dict
from rest_framework.generics import DestroyAPIView
from django.http import Http404
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from news.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from rest_framework.pagination import PageNumberPagination

# Create your views here.
from .models import Posts, Category
from news.serializers import PostsSerializer


class NewsAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


class PostsAPIList(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = NewsAPIListPagination


class PostsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = (IsAuthenticated, ) 


class PostsAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = (IsAdminOrReadOnly, )


# class PostsViewSet(viewsets.ModelViewSet):
#     queryset = Posts.objects.all()
#     serializer_class = PostsSerializer

#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
        
#         if not pk:
#             return Posts.objects.all()[:3]
        
#         return Posts.objects.filter(pk=pk)

#     @action(methods=['get'], detail=True)
#     def category(self, request, pk=None):
#         cats = Category.objects.get(pk=pk)
#         return Response({'cats': cats.name})


# class PostsAPIDetailVeiw(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Posts.objects.all()
#     serializer_class = PostsSerializer