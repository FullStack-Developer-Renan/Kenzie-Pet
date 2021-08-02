from os import write
from rest_framework import serializers
    

class GroupSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    scientific_name = serializers.CharField()

class CharacteristSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    age = serializers.FloatField()
    weight = serializers.FloatField()
    sex = serializers.CharField()
    group = GroupSerializer()
    characteristics = CharacteristSerializer(many=True)
    

    
# from rest_framework import serializers
# from collections import OrderedDict

# class SimpleSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     age = serializers.IntegerField(required=True)
    
# class ArtistSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(required=False)
#     formed_in = serializers.IntegerField(required=False)
#     status = serializers.CharField(required=False)
    
# class SongSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     artist = ArtistSerializer()
    
# class SongSimpleSerializer(serializers.Serializer):    
#     title = serializers.CharField()
    
    
# class ArtistSongsSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     formed_in = serializers.IntegerField()
#     status = serializers.CharField()
#     musics = SongSimpleSerializer(many=True, source='songs')
#     total_songs = serializers.SerializerMethodField()
    
#     def get_total_songs(self, obj):
#         if (isinstance(obj, OrderedDict)):
#             return 0
#         return { 'count': obj.songs.count()}
    
# class PlaylistSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     songs = SongSerializer(many=True)