from django.contrib import admin

# Register your models here.

from .models import TaskList, Task
# Register your models here.
admin.site.register(TaskList)
admin.site.register(Task)