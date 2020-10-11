from rest_framework import serializers
from post.models import Snippet,LANGUAGES_CHOICE,STYLES_CHOICE
from django.contrib.auth.models import User,Group

class UserSerailizer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ['url','username','email','groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ['url','name']


# class SnippetSerializer(serializers.Serializer):
# 	id = serializers.IntegerField(read_only=True)
# 	title = serializers.CharField(required=False,allow_blank=True,max_length=100)
# 	code=  serializers.CharField(style={'base_template':'textarea.html'})
# 	linenos = serializers.BooleanField(required=False)
# 	language = serializers.ChoiceField(choices=LANGUAGES_CHOICE,default='python')
# 	style = serializers.ChoiceField(choices=STYLES_CHOICE,default='friendly')

# 	def create(self,validated_data):
# 		return Snippet.objects.create(**validated_data)

# 	def update(self,instance,validated_data):
# 		instance.title = validated_data.get('title',instance.title)
# 		instance.code = validated_data.get('code',instance.code)
# 		instance.linenos = validated_data.get('linenos',instance.linenos)
# 		instance.language = validated_data.get('language',instance.language)
# 		instance.style = validated_data.get('style',instance.style)
# 		instance.save()
# 		return instance

class SnippetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Snippet
		fields = '__all__'