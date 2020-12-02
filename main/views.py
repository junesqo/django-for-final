from django.shortcuts import render, redirect
from .models import Course
from .forms import CourseForm


def index(request):
    courses = Course.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница', 'courses': courses})


def about(request):
    return render(request, 'main/about.html')

def add(request):
    error = ''
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Ошибка"


    form = CourseForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add.html', context)