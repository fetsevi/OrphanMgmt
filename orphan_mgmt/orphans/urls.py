from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    OrphanListCreateView, CourseListCreateView,
    OrphanDetailView, CourseDetailview,
    GoalCreateView, EnrollmentListCreateView,
    GoalDetailView, EnrollmentDetailView,
    RegisterView, LogoutView
)

urlpatterns = [
    
    #Auth
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    
    # Orphan endpoints
    path('orphans/', OrphanListCreateView.as_view(), name='orphan-list-create'),
    path('orphans/<int:pk>/', OrphanDetailView.as_view(), name='orphan-detail'),
    
    # Course endpoints
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetailview.as_view(), name='course-detail'),
    
    # Goal endpoints
    path('orphans/<int:pk>/goal/', GoalCreateView.as_view(), name='orphan-goal-create'),
    path('goals/<int:pk>/', GoalDetailView.as_view(), name='goal-detail'),
    
    # Enrollment endpoints
    path('enrollments/', EnrollmentListCreateView.as_view(), name='enrollment-list-create'),
    path('enrollments/<int:pk>/', EnrollmentDetailView.as_view(), name='enrollment-detail'),
    
]
