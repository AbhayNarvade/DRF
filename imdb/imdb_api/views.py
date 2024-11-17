from .serializers import watchlistserializer , streamplatformserializer

# Django 

from django.shortcuts import render
from django.http import HttpResponse , JsonResponse , Http404

# Models

from .models import watchlist , streamplatform

# django rest framework

from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.reverse import reverse

# **************************************************************************



# here are different approach of the code that we can used such as function base class base views etc 

# Function base view code 

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'watchlist': reverse('movie-list', request=request, format=format),
        'streamplatform': reverse('stream-platform', request=request, format=format)
    })


@api_view(['GET'])
def movie_list(request):
    movieslist = watchlist.objects.all()
    # print(movieslist)
    serializer =  watchlistserializer(movieslist, many = True)
    return Response (serializer.data)

@api_view(['GET'])
def movie_detail(request , pk):
    moviedetail = watchlist.objects.get(pk = pk)
    # print(moviedetail)
    serializer =  watchlistserializer(moviedetail)
    return Response (serializer.data)



# @api_view(['GET', 'POST'])
# def stream_list(request):
#     if request.method =='GET':
#         streamlist = streamplatform.objects.all()
#         # print(streamlist)
#         serializer =  streamplatformserializer(streamlist, many = True)
#         return Response (serializer.data,status=status.HTTP_200_OK)
    
#     elif request.method =='POST':
#         serializer = streamplatformserializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# @api_view(['GET','POST','PUT', 'DELETE'])
# def stream_detail(request , pk):
#     try:
#        streamdetail = streamplatform.objects.get(pk = pk)
#     except streamplatform.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    

#     if request.method == 'GET':
#         serializer = streamplatformserializer(streamdetail)
#         # print(serializer)
#         return Response(serializer.data ,status=status.HTTP_200_OK)


#     elif request.method == 'POST':
#         serializer = streamplatformserializer( data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data ,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'PUT':
#         serializer = streamplatformserializer(streamdetail, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data ,status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


#     elif request.method == 'DELETE':
#         streamdetail.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# class Base View 


# class StreamPlatformList(APIView):
#     """
#     List all streamplatformserializer, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         streamlist = streamplatform.objects.all()
#         # print(streamlist)
#         serializer =  streamplatformserializer(streamlist, many = True)
#         return Response (serializer.data,status=status.HTTP_200_OK) 

#     def post(self, request, format=None):
#         serializer = streamplatformserializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class StreamPlatformDetail(APIView):
#     """
#     Retrieve, update or delete a streamplatformserializer instance.
#     """

#     def get_object(self, pk):
#         try:
#             return streamplatform.objects.get(pk = pk)
#         except streamplatform.DoesNotExist:
#             raise Http404
        

#     def get(self , request, pk, format=None):
#         streamdetail = self.get_object(pk)
#         serializer = streamplatformserializer(streamdetail)
#         # print(serializer)
#         return Response(serializer.data ,status=status.HTTP_200_OK)

#     def put(self , request, pk, format=None):
#         streamdetail = self.get_object(pk)
#         serializer = streamplatformserializer(streamdetail, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data ,status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self , request, pk, format=None):
#         streamdetail = self.get_object(pk)
#         streamdetail.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




# Using Mixing build Api


# class StreamPlatformList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     """
#     List all streamplatformserializer, or create a new snippet.
#     """

#     queryset = streamplatform.objects.all()
#     serializer_class = streamplatformserializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)



# class StreamPlatformDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     """
#     Retrieve, update or delete a streamplatformserializer instance.
#     """


#     queryset = streamplatform.objects.all()
#     serializer_class = streamplatformserializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


#  Using genric 


class StreamPlatformList(generics.ListCreateAPIView):
    """
    List all streamplatformserializer, or create a new snippet.
    """

    queryset = streamplatform.objects.all()
    serializer_class = streamplatformserializer





class StreamPlatformDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a streamplatformserializer instance.
    """


    queryset = streamplatform.objects.all()
    serializer_class = streamplatformserializer


