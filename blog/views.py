from django.shortcuts import render
from rest_framework import views, response, status
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Post
from .serializers import PostSerializer


class PostListAPIView(views.APIView):
    parser_classes = (MultiPartParser, FormParser) # allows the view to handle multipart/form-data requests.

    def get(self, request, *args, **kwargs):
        print("args:", args)
        print("kwargs:", kwargs)
        
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
