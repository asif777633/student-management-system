from django import forms
from .models import Program, Department, Semester, Course

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['name']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['program', 'dept_name']

class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ['program', 'department', 'name']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['semester', 'course_code', 'course_name', 'credits']
