from django.db import models


class Exercise(models.Model):
    id_app = models.PositiveSmallIntegerField()
    id_exercise = models.PositiveSmallIntegerField()
    scoremax_possible = models.PositiveSmallIntegerField()


class Student(models.Model):
    id_student = models.PositiveSmallIntegerField()
    id_school = models.PositiveSmallIntegerField()
    id_class = models.CharField(max_length=20)


class Scores(models.Model):
    exercise = models.ForeignKey(Exercise)
    student = models.ForeignKey(Student)
    date = models.DateTimeField()
    score = models.PositiveSmallIntegerField()
