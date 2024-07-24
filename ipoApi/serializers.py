from rest_framework import serializers
from ipoApi.models import IpoInfo


#serializers
class IpoSerializers(serializers.HyperlinkedModelSerializer):

   class Meta :
         model = IpoInfo
         fields  = "__all__"