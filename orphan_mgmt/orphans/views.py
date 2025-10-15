from rest_framework import generics, permissions
from .models import Orphan, Course, Goal, Enrollment
from .serializers import OrphanSerializer, CourseSerializer, GoalSerializer, EnrollmentSerializer, RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

User = get_user_model()

# ORPHANS CRUD

class OrphanListCreateView(generics.ListCreateAPIView):
    """Handles GET (list all orphans) & POST (create new orphan)"""
    queryset = Orphan.objects.all()
    serializer_class = OrphanSerializer
    permission_classes = [IsAuthenticated]

    
class OrphanDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Handles GET single orphan, PUT (update), DELETE"""
    queryset = Orphan.objects.all()
    serializer_class = OrphanSerializer
    permission_classes = [IsAuthenticated]

    
# COURSES CRUD

class CourseListCreateView(generics.ListCreateAPIView):
    """Handles GET (list all courses) & POST (create new course)"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    
class CourseDetailview(generics.RetrieveUpdateDestroyAPIView):
    """Handles GET single course, PUT (update), DELETE"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    
# GOAL CRUD

class GoalCreateView(generics.CreateAPIView):
    """Create a Goal for a specific orphan"""
    serializer_class = GoalSerializer
    permission_classes = [IsAuthenticated]
    
class GoalDetailView(generics.RetrieveUpdateDestroyAPIView):
    """GET, PUT, DELETE orphan goal"""
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    permission_classes = [IsAuthenticated]

    
# ENROLLMENT CRUD

class EnrollmentListCreateView(generics.ListCreateAPIView):
    """GET all enrollments or POST new enrollment"""
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]

    
class EnrollmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]

    

# Views for Register, Login, Logout

class RegisterView(generics.CreateAPIView):
    """Register New user"""
    queryset=User.objects.all()
    serializer_class=RegisterSerializer
    permission_classes=[permissions.AllowAny]
    
class LogoutView(generics.GenericAPIView):
    """Logout by blacklisting the refresh token"""
    permission_classes=[permissions.IsAuthenticated]
    
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Successfully logged out"}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=400)
        

# Home page view

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
 

