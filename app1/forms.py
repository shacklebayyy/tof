from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['fname', 'sname', 'adm', 'age', 'classs', 'stream', 'mistake', 'punshmentgiven', 'picture']
