from django.db import models


class Exercise(models.Model):
    id_app = models.PositiveSmallIntegerField()
    id_exercise = models.PositiveSmallIntegerField()
    scoremax_possible = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return self.id_app, self.id_exercise


class Student(models.Model):
    id_student = models.PositiveSmallIntegerField()
    id_school = models.PositiveSmallIntegerField()
    id_class = models.CharField(max_length=20)

    class Meta:
        ordering = ["id_student"]

    def __unicode__(self):
        return self.id_student


class Score(models.Model):
    exercise = models.ForeignKey(Exercise)
    student = models.ForeignKey(Student)
    date = models.DateTimeField()
    score = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return self.student, self.date, self.exercise
