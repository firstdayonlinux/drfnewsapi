from rest_framework import serializers
from .models import Posts
from rest_framework.renderers import JSONRenderer


class PostsSerializer(serializers.ModelSerializer):
        user = serializers.HiddenField(default=serializers.CurrentUserDefault())

        class Meta:
            model = Posts
            fields = '__all__'