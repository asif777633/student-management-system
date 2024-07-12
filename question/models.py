from django.db import models
from django.urls import reverse


class Exam(models.Model):
    university_name = models.CharField(max_length=100, null=True, blank=True)
    subject_name = models.CharField(max_length=100, null=True, blank=True)
    department_name = models.CharField(max_length=100, null=True, blank=True)
    semester_name = models.CharField(max_length=50, null=True, blank=True)
    batch_number = models.CharField(max_length=20, null=True, blank=True)
    course_code = models.CharField(max_length=20, null=True, blank=True)
    time = models.CharField(max_length=20,null=True, blank=True)
    marks = models.IntegerField(null=True, blank=True)

    # Define fields for each question
    q1_number = models.IntegerField(null=True, blank=True)
    q1_description = models.TextField(null=True, blank=True)
    q1_marks = models.IntegerField(null=True, blank=True)
    
    q2_number = models.IntegerField(null=True, blank=True)
    q2_description = models.TextField(null=True, blank=True)
    q2_marks = models.IntegerField(null=True, blank=True)
    
    q3_number = models.IntegerField(null=True, blank=True)
    q3_description = models.TextField(null=True, blank=True)
    q3_marks = models.IntegerField(null=True, blank=True)
    
    q4_number = models.IntegerField(null=True, blank=True)
    q4_description = models.TextField(null=True, blank=True)
    q4_marks = models.IntegerField(null=True, blank=True)
    
    q5_number = models.IntegerField(null=True, blank=True)
    q5_description = models.TextField(null=True, blank=True)
    q5_marks = models.IntegerField(null=True, blank=True)
    
    q6_number = models.IntegerField(null=True, blank=True)
    q6_description = models.TextField(null=True, blank=True)
    q6_marks = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"University: {self.university_name}, Course: {self.course_code}, Batch: {self.batch_number}"
    def get_absolute_url(self):
        return reverse('exam-detail', kwargs={'pk': self.pk})


