from django.contrib import admin

from . models import subjects, courseOffered


class subjectsAdmin(admin.ModelAdmin):
    list_display = ['name']

class CourseofferedAdmin(admin.ModelAdmin):
    list_display = ['courseSubject','courseName','courseDuration','coursePrice']


admin.site.register(subjects,subjectsAdmin)
admin.site.register(courseOffered,CourseofferedAdmin)

