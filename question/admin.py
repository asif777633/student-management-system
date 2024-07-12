from django.contrib import admin
from .models import Exam
# Register your models here.

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        "university_name"
    ]