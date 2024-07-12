from django import forms
from .models import Exam

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = [
            'university_name', 'subject_name', 'department_name', 'semester_name',
            'batch_number', 'course_code', 'time', 'marks',
            'q1_number', 'q1_description', 'q1_marks',
            'q2_number', 'q2_description', 'q2_marks',
            'q3_number', 'q3_description', 'q3_marks',
            'q4_number', 'q4_description', 'q4_marks',
            'q5_number', 'q5_description', 'q5_marks',
            'q6_number', 'q6_description', 'q6_marks'
        ]
        widgets = {
            'university_name': forms.TextInput(attrs={'class': 'form-control'}),
            'subject_name': forms.TextInput(attrs={'class': 'form-control'}),
            'department_name': forms.TextInput(attrs={'class': 'form-control'}),
            'semester_name': forms.TextInput(attrs={'class': 'form-control'}),
            'batch_number': forms.TextInput(attrs={'class': 'form-control'}),
            'course_code': forms.TextInput(attrs={'class': 'form-control'}),
            'time': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'marks': forms.NumberInput(attrs={'class': 'form-control'}),
            'q1_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'q1_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'q1_marks': forms.NumberInput(attrs={'class': 'form-control'}),
            'q2_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'q2_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'q2_marks': forms.NumberInput(attrs={'class': 'form-control'}),
            'q3_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'q3_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'q3_marks': forms.NumberInput(attrs={'class': 'form-control'}),
            'q4_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'q4_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'q4_marks': forms.NumberInput(attrs={'class': 'form-control'}),
            'q5_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'q5_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'q5_marks': forms.NumberInput(attrs={'class': 'form-control'}),
            'q6_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'q6_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'q6_marks': forms.NumberInput(attrs={'class': 'form-control'}),
        }