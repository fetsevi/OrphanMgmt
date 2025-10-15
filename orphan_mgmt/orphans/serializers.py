# Orphans serializer

from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Orphan, Course, Goal, Enrollment

User = get_user_model()

class OrphanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orphan
        fields = '__all__' # include all fields
        
# Course serializer
        
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        
# Goal serializer

class GoalSerializer(serializers.ModelSerializer):
    orphan_name = serializers.ReadOnlyField(source='orphan.name')
   
    class Meta:
        model = Goal
        fields = '__all__'

# Enrollment Serializer

class EnrollmentSerializer(serializers.ModelSerializer):
    orphan_name = serializers.ReadOnlyField(source='orphan.name')
    course_title = serializers.ReadOnlyField(source='course.title')
    
    class Meta:
        model = Enrollment
        fields = '__all__'
        
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'role']
        
        def create(self, validated_data):
            user = User.objects.create_user(
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password'],
                role=validated_data.get('role', 'trainer')
            )
            return user
        

        