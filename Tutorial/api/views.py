from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from .serializer import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ques','created']
    search_fields = ['ques',]

class ReplyView(APIView):
    def get(self,request,format=None):
        qs = Reply.objects.all()
        serializer = ReplySerializer(qs,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ReplyMix(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
