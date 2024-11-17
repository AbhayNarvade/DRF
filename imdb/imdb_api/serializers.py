from rest_framework import serializers
from .models import streamplatform , watchlist

# class watchlistserializer (serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title =  serializers.CharField(max_length=50)
#     storyline = serializers.CharField(max_length=100)
#     # platform = serializers.ForeignKey(streamplatform , on_delete= models.CASCADE)
#     active =  serializers.BooleanField(default=True)
#     created = serializers.DateTimeField()

#     def create(self, validated_data):
#         """
#         Create and return a new `watchlist` instance, given the validated data.
#         """
#         return watchlist.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `watchlist` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.storyline = validated_data.get('storyline', instance.storyline)
#         instance.active = validated_data.get('active', instance.active)
#         instance.created = validated_data.get('created', instance.created)
#         instance.save()
#         return instance


# class streamplatformserializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=50)
#     about = serializers.CharField(max_length=100)
#     website =  serializers.URLField(max_length=100)
# 
#     def create(self, validated_data):
#         """
#         Create and return a new `streamplatform` instance, given the validated data.
#         """
#         return streamplatform.objects.create(**validated_data)
# 
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `streamplatform` instance, given the validated data.
#         """
#         instance.name = validated_data.get('name', instance.name)
#         instance.about = validated_data.get('about', instance.about)
#         instance.website = validated_data.get('website', instance.website)
#         instance.save()
#         return instance


class streamplatformserializer (serializers.ModelSerializer):
    class Meta :
        model = streamplatform
        fields = '__all__'



class watchlistserializer(serializers.ModelSerializer):
    class Meta:
        model = watchlist
        # fields = ['id', 'title', 'storyline', 'platform', 'active', 'created']
        fields = '__all__'