from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform , Review


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        fields = "__all__"



class WatchListSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many = True,read_only =True)
    class Meta:
        model = WatchList
        fields = "__all__"
        # fields = ['id','name','description']
    #     # exclude = ['active']
    
    def get_len_name(self,object):
       return len(object.title)
   
   
class StreamPlatformSerializer(serializers.ModelSerializer):
    #watchlist = WatchListSerializer(many=True,read_only=True)
    #watchlist = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    watchlist = serializers.HyperlinkedRelatedField(many=True,read_only=True , view_name='movie-detail')
   
    class Meta:
        model = StreamPlatform
        fields = "__all__"
        
  

   
   
   
   
   
   
   
    # def validate_name(self,value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError('Movie name should be at least 2 characters long.')
    #     return value
        
    # def validate(self,data):
    #     if data['title'] == data['description']:
    #         raise serializers.ValidationError('Title and description should not be the same.')
    #     else:
    #         return data


# def name_length(value):

#     if len(value) < 2:
#         raise serializers.ValidationError('Movie name should be at least 2 characters long.')
    
    
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validates = [name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self,validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self,instance,validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.description = validated_data.get('description',instance.description)
#         instance.active = validated_data.get('active',instance.active)
#         instance.save()
#         return instance
    
#     def validate_name(self,value):
#         if len(value) < 2:
#             raise serializers.ValidationError('Movie name should be at least 2 characters long.')
#         return value
        
#     def validate(self,data):
#         if data['title'] == data['description']:
#             raise serializers.ValidationError('Title and description should not be the same.')
#         else:
#             return data