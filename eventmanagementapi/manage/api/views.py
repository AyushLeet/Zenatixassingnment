from django.shortcuts import render
from rest_framework import viewsets
from api.models import Event,User
from api.serializers import EventSerializer,UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
class EventViewSet(viewsets.ModelViewSet):
    queryset= Event.objects.all()
    serializer_class=EventSerializer
    
    #events/usersid/
    @action(detail=True,methods=['get'])
    def user(self,request,pk=None):   
        try:                
            event=Event.objects.get(pk=pk)
            user=User.objects.filter(event=event)
            user_serializer=UserSerializer(user,many=True,context={'request':request})
            return Response(user_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Event might not exists !! Error'
            })


class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer