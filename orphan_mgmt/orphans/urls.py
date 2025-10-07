from django.urls import path
from .views import (
    OrphanListCreateView, CourseListCreateView,
    OrphanDetailView, CourseDetailview,
    GoalCreateView, EnrollmentListCreateView,
    GoalDetailView, EnrollmentDetailView
)

urlpatterns = [
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
