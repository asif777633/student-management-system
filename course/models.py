from django.db import models


# Create your models here.

"""
Program under department 
Department and Program under semi
"""

class Program(models.Model):
    PROGRAM_CHOICES = [
        ('BSc', 'Bachelor of Science'),
        ('MSc', 'Master of Science'),
    ]
    name = models.CharField(max_length=3, choices=PROGRAM_CHOICES, unique=True)

    def __str__(self):
        return self.get_name_display()

    
class Department(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='department')
    dept_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.dept_name}"


class Semester(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='semesters')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='semesters')
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.program} - {self.name}"

class Course(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='courses')
    course_code = models.CharField(max_length=10)
    course_name = models.CharField(max_length=100)
    credits = models.IntegerField()

    def __str__(self):
        return f"{self.course_code} - {self.course_name} ({self.credits} credits)"
    





