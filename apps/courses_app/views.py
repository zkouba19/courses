from django.shortcuts import render, redirect, HttpResponse
from . import models
# Create your views here.
def index(request):
	courses = models.Courses.objects.all()
	context = {
		"courses": courses
	}
	print courses

	return render(request, 'courses_app/index.html', context)

def process(request):
	if request.method == "POST":
		models.Courses.objects.create(name = request.POST['name'], description = request.POST['description'])
		return redirect('/')

def remove(request, id):
	if request.method == "GET":

		courses = models.Courses.objects.get(id = id)
		context = {
			'name': courses.name,
			'description': courses.description,
			'created_at': courses.created_at,
			'id': courses.id
		}
	return render(request, 'courses_app/courses.html', context)

def delete(request, id):
	if request.method == "GET":
		models.Courses.objects.filter(id = id).delete()
	return redirect('/')

def go_back(request, id):
	if request.method == "GET":
		return redirect('/')