from django import forms
import django_filters
from .models import Lesson


class LessonFilter(django_filters.FilterSet):
    project_name = django_filters.CharFilter(lookup_expr='icontains')
    project_number = django_filters.CharFilter(lookup_expr='icontains')
    client = django_filters.CharFilter(lookup_expr='icontains')
    project_location = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    division = django_filters.CharFilter(lookup_expr='icontains')
    market_sector = django_filters.CharFilter(lookup_expr='icontains')
    discipline = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Lesson
        fields = [
                'project_name', 'project_number','client','project_location', 'description',
                'division','market_sector','discipline','author',
        ]