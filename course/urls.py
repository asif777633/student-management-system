from django.urls import path
from .views import (
    ProgramListView, ProgramCreateView,
    DepartmentListView, DepartmentCreateView, DepartmentUpdateView,
    SemesterListView, SemesterCreateView, SemesterUpdateView, SemesterDetailView,
    CourseListView, CourseCreateView, CourseUpdateView
)

urlpatterns = [
    # Program URLs
    path('programs/', ProgramListView.as_view(), name='program_list'),
    path('programs/create/', ProgramCreateView.as_view(), name='program_create'),
    
    # Department URLs
    path('departments/', DepartmentListView.as_view(), name='department_list'),
    path('departments/create/', DepartmentCreateView.as_view(), name='department_create'),
    path('departments/<int:pk>/update/', DepartmentUpdateView.as_view(), name='department_update'),
    
    # Semester URLs
    path('semesters/', SemesterListView.as_view(), name='semester_list'),
    path('semesters/create/', SemesterCreateView.as_view(), name='semester_create'),
    path('semesters/<int:pk>/update/', SemesterUpdateView.as_view(), name='semester_update'),
    path('semester/<int:pk>/', SemesterDetailView.as_view(), name='semester-detail'),

    
    # Course URLs
    path('courses/', CourseListView.as_view(), name='course_list'),
    path('courses/create/', CourseCreateView.as_view(), name='course_create'),
    path('courses/<int:pk>/update/', CourseUpdateView.as_view(), name='course_update'),
]
