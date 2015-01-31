from django.db import models
from django.contrib.auth.models import User


class Exercise(models.Model):
    # id primary key
    id_app = models.PositiveSmallIntegerField()
    id_exercise = models.PositiveSmallIntegerField()
    scoremax_possible = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ('id_app', 'id_exercise',)

    def __unicode__(self):
        exer_return = (str(self.id_app) + ' ' + str(self.id_exercise) + ' ' + str(self.scoremax_possible))
        return exer_return


class Student(models.Model):
    # id primary key
    id_student = models.PositiveSmallIntegerField(unique=True)
    id_school = models.PositiveSmallIntegerField()
    id_class = models.CharField(max_length=20)

    class Meta:
        ordering = ["id_student"]

    def __unicode__(self):
        std_return = (str(self.id_student) + ' ' + str(self.id_school) + ' ' + self.id_class)
        return std_return


class Score(models.Model):
    # id primary key
    exercise = models.ForeignKey(Exercise)
    student = models.ForeignKey(Student)
    date = models.DateTimeField()
    score = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ('student', 'date', 'exercise')

    def __unicode__(self):
        score_return = (str(self.student) + ' - ' + str(self.date) + ' - ' + str(self.exercise))
        return score_return
