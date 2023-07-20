from django.contrib import admin

# Register your models here.
# register school and fee models
from school.models import Fee, Student

admin.site.register(Student)
admin.site.register(Fee)
