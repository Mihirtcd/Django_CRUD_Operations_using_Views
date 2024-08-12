from django import forms
from .models import Subject,Student,Teacher

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'description']
        
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_name', 'age','email','contact','address','dob','profile_picture','enrolled_subject']
        
class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'email','contact','subjects','students']
        