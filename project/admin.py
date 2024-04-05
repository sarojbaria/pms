from django.contrib import admin
from .models import Project,Country,City,Books, user_task,Task

# Register your models here.
admin.site.register(Project)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Books)
admin.site.register(user_task)
admin.site.register(Task)