from django.contrib import admin
from predict_site.models import Users, Courses, StuScore


# Register your models here.


class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'stu_no', 'name', 'gender', 'major', 'portrait', 'mail', 'status','Uphy', 'Amath', 'Lalg', 'C', 'Cpp')


class CoursesAdmin(admin.ModelAdmin):
    list_display = ('name', 'intro', 'course_id')

class StuScoreAdmin(admin.ModelAdmin):
    list_display = ('score_predict','score_actual','stu_no','course_id','predict_accuracy_rating')


admin.site.register(Users, UsersAdmin)
admin.site.register(Courses, CoursesAdmin)
admin.site.register(StuScore,StuScoreAdmin)
