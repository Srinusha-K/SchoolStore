from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import StudentCreationForm
from .models import St_data, Courses


def student_create_view(request):
    form = StudentCreationForm()
    if request.method == 'POST':
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Order Confirmed")
            return redirect('student_add')
    return render(request, 'home.html', {'form': form})


def student_update_view(request, pk):
    student = get_object_or_404(St_data, pk=pk)
    form = StudentCreationForm(instance=student)
    if request.method == 'POST':
        form = StudentCreationForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_change', pk=pk)
    return render(request, 'home.html', {'form': form})


# AJAX
def load_courses(request):
    department_id = request.GET.get('department_id')
    courses = Courses.objects.filter(department_id=department_id).all()
    #return render(request, 'courses_dropdown_list.html', {'courses': courses})
    return JsonResponse(list(courses.values('id', 'name')), safe=False)


