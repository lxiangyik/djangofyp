from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.forms import BooleanField

# Create your models here.


class Staff(models.Model):
    staffFirstName = models.CharField(max_length=50)
    staffLastName = models.CharField(max_length=50)
    staffTp = models.CharField(max_length=8)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.staffTp


class Course(models.Model):
    courseName = models.CharField(max_length=100)

    def __str__(self):
        return self.courseName


class Subject(models.Model):
    subName = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.subName


class Classes(models.Model):
    classesDate = models.DateField
    classesStartTime = models.TimeField
    classesEndTime = models.TimeField
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.id


class Student(models.Model):
    studFirstName = models.CharField(max_length=50)
    studLastName = models.CharField(max_length=50)
    tp = models.CharField(max_length=8)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.tp


class Attendance(models.Model):
    attDate = models.DateField
    attState = BooleanField
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class Announcement(models.Model):
    announceTitle = models.CharField(max_length=100)
    announceDescription = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.announceTitle

class FacePattern(models.Model):
    studFacePat = models.CharField(max_length=1000, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.id