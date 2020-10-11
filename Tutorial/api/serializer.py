from rest_framework import serializers
from Tutorial.models import *

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Question
        fields = '__all__'

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'
