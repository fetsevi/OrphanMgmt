from rest_framework import generics
from .models import Orphan, Course, Goal, Enrollment
from .serializers import OrphanSerializer, CourseSerializer, GoalSerializer, EnrollmentSerializer

# ORPHANS CRUD

class OrphanListCreateView(generics.ListCreateAPIView):
    """Handles GET (list all orphans) & POST (create new orphan)"""
    queryset = Orphan.objects.all()
    serializer_class = OrphanSerializer
    
class OrphanDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Handles GET single orphan, PUT (update), DELETE"""
    queryset = Orphan.objects.all()
    serializer_class = OrphanSerializer
    
# COURSES CRUD

class CourseListCreateView(generics.ListCreateAPIView):
    """Handles GET (list all courses) & POST (create new course)"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
class CourseDetailview(generics.RetrieveUpdateDestroyAPIView):
    """Handles GET single course, PUT (update), DELETE"""
    queryset = Course.objects.all
    serializer_class = CourseSerializer
    
# GOAL CRUD

class GoalCreateView(generics.CreateAPIView):
    """Create a Goal for a specific orphan"""
    serializer_class = GoalSerializer
    
class GoalDetailView(generics.RetrieveUpdateDestroyAPIView):
    """GET, PUT, DELETE orphan goal"""
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    
# ENROLLMENT CRUD

class EnrollmentListCreateView(generics.ListCreateAPIView):
    """GET all enrollments or POST new enrollment"""
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    
class EnrollmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.all
    serializer_class = EnrollmentSerializer
    

