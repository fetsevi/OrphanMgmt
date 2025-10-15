from django.contrib.auth.models import AbstractUser
from django.db import models

# Orphans model 

class Orphan(models.Model):
    """Model to store orphan's personal information"""
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    nationality = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True) # auto set when created
    
    def __str__(self):
        return self.name

# Courses model

class Course(models.Model):
   """Model to represent courses orphans can be enrolled in"""
   title = models.CharField(max_length=100)
   description = models.TextField()
   duration = models.IntegerField()
   
   def __str__(self):
       return self.title 

# Goal model    
class Goal(models.Model):
    """Each Orphan's personal goal"""
    orphan = models.OneToOneField(Orphan, on_delete=models.CASCADE, related_name='goal')
    description = models.TextField()
    is_achieved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.orphan.name}'s goal"
    
class Enrollment(models.Model):
    """Link between Orphan and Course"""
    orphan = models.ForeignKey(Orphan, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    progress = models.IntegerField(default=0) # progress percentage
    enrolled_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('orphan', 'course') # prevent double enrollement
        
    def __str__(self):
        return f"{self.orphan.name} enrolled in {self.course.title}"
    
# Customer User

class User(AbstractUser):
    """Custom User model with role field"""
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('trainer', 'Trainer'),
    )
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Trainer')
    
    def __str__(self):
        return f"{self.username} ({self.role})"