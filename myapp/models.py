from django.db import models
import os
import uuid
from uuid import uuid4

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    description = models.TextField()

    def __str__(self):
        return self.name

def user_directory_path(instance, filename):
    # Extract the file extension
    ext = filename.split('.')[-1]
    # Generate a unique filename using UUID
    filename = f"{uuid4().hex}.{ext}"
    # Construct the file path
    return os.path.join('user_{0}'.format(instance.id), filename)

class Student(models.Model):
    stu_id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    student_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField(max_length=254, unique=True)
    contact = models.CharField(max_length=15)
    address = models.TextField(null =True,blank= True)
    dob = models.DateField()
    joining_date_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    profile_picture = models.ImageField(upload_to=user_directory_path,null=True,blank=True)
    enrolled_subject = models.ManyToManyField(Subject, related_name='enrolled_students')
    
    def save(self, *args, **kwargs):
        if not self.stu_id:
            self.stu_id = uuid4()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.student_name

class Teacher(models.Model):
    teach_id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    contact = models.CharField(max_length=15)
    subjects = models.ForeignKey(Subject, related_name='teaching_staff', on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name='teachers')

    def __str__(self):
        return self.name