from django.shortcuts import render
from myapp.models import Student
# Create your views here.

def list_all(request):
	myapp = Student.objects.all().order_by('id')
	return render(request, 'list_all.html', locals())