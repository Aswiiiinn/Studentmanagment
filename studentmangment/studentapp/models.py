from email.policy import default
from re import T
from django.db import models
from django.contrib.auth.models import AbstractUser


from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=55)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Batch(models.Model):
    name = models.CharField(max_length=55)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="batches")
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.course.name}"

class Teacher(models.Model):
    username = models.CharField(max_length=100,null=True)
    password = models.CharField(max_length=100,null=True)
    name = models.CharField(max_length=55)
    batches = models.ManyToManyField(Batch, related_name="teachers")
    courses = models.ManyToManyField(Course, related_name="teachers")
    email = models.EmailField(max_length=34,blank=False)
    def __str__(self):
        return self.name

class Student(models.Model):
    username = models.CharField(max_length=100,blank=False,default=None)
    password = models.CharField(max_length=25,unique=True,null=False,default=None)
    email = models.EmailField(max_length=59,default=None)
    name = models.CharField(max_length=55)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name="students")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="students")
    score = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
class CourseMeterial(models.Model):
    title  = models.CharField(max_length=45)
    course =models.ForeignKey(Course, on_delete=models.CASCADE)
    files = models.FileField(upload_to='course_meterial/')
    uploaded_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    uploaded_at=models.DateTimeField(auto_now_add=True)
class importex(models.Model):
    Student_Name = models.CharField(max_length=100)
    Exam_Name = models.CharField(max_length=150)
    Date = models.CharField(max_length=250)
    Point = models.CharField(max_length=100,null=True,default=None)
class Achivments(models.Model): 
    out = "outstanding"
    vG = "veryGood"
    go ="good"
    av = "average"
    ba ="bad"
    pr ="veryBad"
    class_perfomancechoise = (
        (out,"outstanding"),
        (vG,"veryGood"),
        (go,"good"),
        (av,"average"),
        (ba,"bad"),
        (pr,"veryBad"),)
    S ="S"
    A1 ="A+"
    A2 ="A"
    B1 ="B+"
    B2 ="B"
    C1 ="C+"
    C2 ="C"
    F = "F"
    GradeChoices = (
        (S,"S"),
        (A1,"A+"),
        (A2,"A"),
        (B1,"B+"),
        (B2,"B"),
        (C1,"C+"),
        (C2,"C"),
        (F,"F"),)
    name = models.ForeignKey(Student,on_delete=models.CASCADE)
    score = models.IntegerField(null=True,)
    Grade  = models.CharField(max_length=15,choices=GradeChoices)
    class_perfomance = models.CharField(max_length=20,choices= class_perfomancechoise)
class attandence(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=False)
    
