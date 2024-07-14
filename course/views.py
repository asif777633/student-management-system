from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Program, Department, Semester, Course
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .models import Program, Department, Semester, Course
from .forms import ProgramForm, DepartmentForm, SemesterForm, CourseForm
from django.db import models

class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'course/program_form.html'
    success_url = reverse_lazy('program_list')


class ProgramListView(ListView):
    model = Program
    template_name = 'course/program_list.html'
    context_object_name = 'programs'



# Department Views
class DepartmentListView(ListView):
    model = Department
    template_name = 'course/department_list.html'
    context_object_name = 'departments'

class DepartmentCreateView(CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'course/department_form.html'
    success_url = reverse_lazy('department_list')

class DepartmentUpdateView(UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'course/department_form.html'
    success_url = reverse_lazy('department_list')



# Semester Views
class SemesterListView(ListView):
    model = Semester
    template_name = 'course/semester_list.html'
    context_object_name = 'semesters'

class SemesterCreateView(CreateView):
    model = Semester
    form_class = SemesterForm
    template_name = 'course/semester_form.html'
    success_url = reverse_lazy('semester_list')

class SemesterUpdateView(UpdateView):
    model = Semester
    form_class = SemesterForm
    template_name = 'course/semester_form.html'
    success_url = reverse_lazy('semester_list')


class SemesterDetailView(DetailView):
    model = Semester
    template_name = 'course/semester_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        semester = self.get_object()
        courses = Course.objects.filter(semester=semester)
        total_credits = courses.aggregate(total_credits=models.Sum('credits'))['total_credits']
        
        context['courses'] = courses
        context['total_credits'] = total_credits
        return context



# Course Views
class CourseListView(ListView):
    model = Course
    template_name = 'course/course_list.html'
    context_object_name = 'courses'

class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'course/course_form.html'
    success_url = reverse_lazy('course_list')

class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'course/course_form.html'
    success_url = reverse_lazy('course_list')





