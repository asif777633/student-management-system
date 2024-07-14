from django import forms
from .models import Program, Department, Semester, Course

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['name']
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control'}),
        }

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['program', 'dept_name']
        widgets = {
            'program': forms.Select(attrs={'class': 'form-control'}),
            'dept_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ['program', 'department', 'name']
        widgets = {
            'program': forms.Select(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['semester', 'course_code', 'course_name', 'credits']
        widgets = {
            'semester': forms.Select(attrs={'class': 'form-control'}),
            'course_code': forms.TextInput(attrs={'class': 'form-control'}),
            'course_name': forms.TextInput(attrs={'class': 'form-control'}),
            'credits': forms.NumberInput(attrs={'class': 'form-control'}),
        }
