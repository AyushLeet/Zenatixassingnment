from rest_framework import serializers
from api.models import Event,User
 

#create serializers here
class EventSerializer(serializers.HyperlinkedModelSerializer):
    event_id=serializers.ReadOnlyField()
    class Meta:
        model=Event
        fields="__all__"
        
        
        
class UserSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()    
    class Meta:
        model=User
        fields="__all__"