from rest_framework import serializers
from rest_framework.serializers import Serializer, FileField
from .models import NgoDB,philDB

class ngoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
          model = NgoDB
          fields = ('ngo_name','ngo_loc','ngo_prevWork','ngo_goal','ngo_sector','ngo_pass','ngo_phoneNo')
          
class philSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
          model = philDB
          fields = ('phil_name','phil_email','phil_pass','phil_phoneNo','phil_interest')
          
class NameSerializer(serializers.Serializer):
    cphil = serializers.CharField()
    
class checkDataSerializer(serializers.Serializer):
    cemail = serializers.CharField()
    cpwd = serializers.CharField()