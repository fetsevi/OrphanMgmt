# Orphans serializer

from rest_framework import serializers
from .models import Orphan, Course, Goal, Enrollment

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
        
    

        