from rest_framework import serializers
from course.models import CookingCourse, Pupil
from django.contrib.auth import get_user_model


class ChefSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)
    cooking_courses = serializers.HyperlinkedRelatedField(many=True, view_name='cookingcourse-detail', read_only=True)
    
    #we override Create method
    
    def create(self, validated_data):
        chef = get_user_model().objects.create(
            username = validated_data['username'], 
            email = validated_data['email']
        )
        #we assume there is custom auth model or build-in auth model
        #custom auth model can we set by AUTH_USER_MODEL in settings.py
        chef.set_password(validated_data['password'])
        chef.save()
        return chef
    
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'password', 'cooking_courses')


class PupilSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Pupil
        fields = ('url', 'id', 'name', 'last_name', 'cp', 'country_code')
        
        
class CookingCourseSerializer(serializers.HyperlinkedModelSerializer):
    chef = serializers.ReadOnlyField(source='chef.email')
    pupils = PupilSerializer(read_only=True, many=True)

    class Meta:
        model = CookingCourse
        fields = ('url', 'id', 'chef', 'name', 'description', 'start_date',
                  'end_date', 'pupils')
        