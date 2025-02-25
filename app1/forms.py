from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['fname', 'sname', 'adm', 'age', 'classs', 'stream', 'mistake', 'mistake_1', 'punshmentgiven', 'third_mistake','blackbook','picture']

    def clean_adm(self):
        adm = self.cleaned_data.get('adm')
        if Student.objects.filter(adm=adm).exists():
            raise forms.ValidationError("A student with this admission number already exists.")
        return adm
