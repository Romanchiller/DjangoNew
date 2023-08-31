from django.contrib import admin

from .models import Student, Teacher


class StudentTeachersInline(admin.TabularInline):
    model = Student.teachers.through


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'group']
    inlines = [ StudentTeachersInline, ]



@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject',]
    inlines = [StudentTeachersInline, ]
    exclude = ['students']
    list_filter = ['students']

