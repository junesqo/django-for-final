from .models import Course
from django.forms import ModelForm, TextInput, Textarea


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'category', 'description', 'link']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название',
            }),
            "category": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите категорию',
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание',
            }),
            "link": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вставьте ссылку',
            }),
        }