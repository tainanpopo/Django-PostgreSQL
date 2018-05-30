from django.contrib import admin
from myapp.models import Student
# Register your models here.

class studentAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'sex', 'birthday', 'phone')
	list_filter = ('name',)
	ordering = ('id',)

admin.site.register(Student, studentAdmin)