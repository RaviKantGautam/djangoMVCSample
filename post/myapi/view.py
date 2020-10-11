from rest_framework import viewsets
from rest_framework import permissions
from django.http import HttpResponse,JsonResponse,Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import *
from post.models import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerailizer
	permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer
	permission_classes = [permissions.IsAuthenticated]

@api_view(['GET','POST'])
def snipped_list(request):
	if request.method=='GET':
		snippets = Snippet.objects.all()
		serializer = SnippetSerializer(snippets,many=True)
		# return JsonResponse(serializer.data,safe=False)
		return Response(serializer.data)
	elif request.method=='POST':
		serializer = SnippetSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			# return JsonResponse(serializer.data,status=201)
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		# return JsonResponse(serializer.errors,status=400)
		return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def snippet_detail(request,pk):
	try:
		snippet = Snippet.objects.get(pk=pk)
	except Snippet.DoesNotExist:
		# return HttpResponse(status==404)
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method=='GET':
		serializer = SnippetSerializer(snippet)
		# return JsonResponse(serializer.data)
		return Response(serializer.data)

	elif request.method=='PUT':
		data = JSONParser().parser(request)
		serializer = SnippetSerializer(snippet,data=data)
		if serializer.is_valid():
			serializer.save()
			# return JsonResponse(serializer.data)
			return Response(serializer.data)
		# return JsonResponse(serializer.errors,status==400)
		return Response(status=status.HTTP_400_BAD_REQUEST)

	elif request.method=='DELETE':
		snippet.delete()
		# return HttpResponse(status=204)
		return Response(status=status.HTTP_204_NO_CONTENT)

class SnippetList(APIView):
	def get(self,request,format=None):
		snippet=  Snippet.objects.all()
		serializer = SnippetSerializer(snippet,many=True)
		return Response(serializer.data)

	def post(self,request,format=None):
		snippet = SnippetSerializer(data=request.data)
		if snippet.is_valid():
			snippet.save()
			return Response(snippet.data,status=status.HTTP_201_CREATED)
		return Response(snippet.errors,status=status.HTTP_400_BAD_REQUEST)

class SnippetDetail(APIView):

	def get_object(self,pk):
		try:
			return Snippet.objects.get(pk=pk)
		except Snippet.DoesNotExist:
			raise Http404

	def get(self,request,pk,format=None):
		snippet = self.get_object(pk)
		serializer = SnippetSerializer(snippet)
		return Response(serializer.data)

	def put(self,request,pk,format=None):
		snippet = self.get_object(pk)
		serializer = SnippetSerializer(snippet,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	def delete(self,request,pk,format=None):
		snippet = self.get_object(pk)
		snippet.delete()
		return Response(status=status.HTTP_204_NOT_CONTENT)

class SnippetListMixins(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer

	def get(self,request,*args,**kwargs):
		return self.list(request,*args,**kwargs)

	def post(self,request,*args,**kwargs):
		return self.create(request,*args,**kwargs)

class SnippetDetailMixins(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer

	def get(self,request,*args,**kwargs):
		return self.retrieve(request,*args,**kwargs)

	def put(self,request,*args,**kwargs):
		return self.update(request,*args,**kwargs)

	def delete(self,request,*args,**kwargs):
		return self.destroy(request,*args,**kwargs)

class SnippetListGeneric(generics.ListCreateAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer

class SnippetDetailGeneric(generics.RetrieveUpdateDestroyAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer