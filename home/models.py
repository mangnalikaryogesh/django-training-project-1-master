from django.db import models
from datetime import timedelta

# Create your models here.
class subjects(models.Model):
    name = models.CharField(max_length=30)
    subjectImage = models.ImageField(upload_to="images/")
    
    class Meta:
        verbose_name = "Subjects"
        verbose_name_plural = "Subjects"
        
        
    def __str__(self):
        return self.name
    
    
class courseOffered(models.Model):
    courseSubject = models.ForeignKey(subjects, on_delete=models.CASCADE,related_name="courseoffered")  #PROTECT 
    courseImage = models.ImageField(upload_to="images/")
    courseName = models.CharField(max_length=100)
    courseDuration =  models.DurationField(default=timedelta(hours=3, minutes=30),help_text="Enter the duration of the course in hours and minutes.")
    coursePrice = models.IntegerField(help_text="Enter the price in dollars")
    
    class Meta:
        verbose_name = "Courses Offered"
        verbose_name_plural = "Courses Offered"
        
        
    def __str__(self):
        return self.courseName