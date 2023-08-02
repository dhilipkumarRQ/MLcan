from rest_framework import serializers
from .models import Comment, Activity_Quote_Repair_List
from account.models import User
from container.models import Container
from account.serializers import UserSerializers
from mlcan.config import COMMENT_ORIGIN_ALLOWED


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializers(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)
    
    class Meta:
        model=Comment
        fields = ['id','user_id','user','comment_text','comment_type','modified_datetime']
        

    def create(self, validated_data):
        object = None
        if validated_data['comment_origin'] == COMMENT_ORIGIN_ALLOWED[0]:
            object = Container.objects.get(id=validated_data['comment_origin_id'])
        else:
            object = Activity_Quote_Repair_List.objects.get(id=validated_data['comment_origin_id'])
        validated_data.pop('comment_origin')
        validated_data.pop('comment_origin_id')
        return Comment.objects.create(content_object=object,**validated_data)