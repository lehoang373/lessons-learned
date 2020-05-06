from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from .filters import LessonFilter
from django.http import HttpResponse
import csv
from datetime import datetime


now = timezone.now()

def home(request):
    return render(request, 'll/home.html',
                  {'ll': home})

@login_required
def lesson_delete(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    lesson.delete()
    return redirect('ll:lesson_list')

@login_required
def lesson_list(request):
    lessons = Lesson.objects.filter(created_date__lte=timezone.now())
    return render(request, 'll/lesson_list.html', {'lessons': lessons})

@login_required
def lesson_new(request):
    if request.method == "POST":
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.created_date = timezone.now()
            lesson.save()
            lessons = Lesson.objects.filter(created_date__lte=timezone.now())
            return render(request, 'll/lesson_list.html',
                          {'lessons': lessons})
    else:
        form = LessonForm()
        # print("Else")
    return render(request, 'll/lesson_new.html', {'form': form})

@login_required
def lesson_edit(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    if request.method == "POST":
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            lesson = form.save()
            # lesson.customer = lesson.id
            lesson.updated_date = timezone.now()
            lesson.save()
            lessons = Lesson.objects.filter(created_date__lte=timezone.now())
            return render(request, 'll/lesson_list.html', {'lessons': lessons})
    else:
        # print("else")
        form = LessonForm(instance=lesson)
    return render(request, 'll/lesson_edit.html', {'form': form})

def search(request):
    lesson_list = Lesson.objects.all()
    lesson_filter = LessonFilter(request.GET, queryset=lesson_list)
    return render(request, 'search/user_list.html', {'filter': lesson_filter})

def export_Lessons_toCSV(request):
    fields = [f.name for f in Lesson._meta.fields]
    timestamp = datetime.now()
    timeappend = timestamp.strftime("%x")
    response = HttpResponse(content_type="text/csv")
    response[
        "Content-Disposition"
    ] = f"attachment; filename={timeappend}-Lesson.csv"
    writer = csv.writer(response)

    writer.writerow(fields)
    for row in Lesson.objects.values(*fields):
        writer.writerow([row[field] for field in fields])
    return response