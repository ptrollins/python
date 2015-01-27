from django.db import models


class Exercise(models.Model):
    # id primary key
    id_app = models.PositiveSmallIntegerField()
    id_exercise = models.PositiveSmallIntegerField()
    scoremax_possible = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return self.id_app, self.id_exercise


class Student(models.Model):
    # id primary key
    id_student = models.PositiveSmallIntegerField()
    id_school = models.PositiveSmallIntegerField()
    id_class = models.CharField(max_length=20)

    class Meta:
        ordering = ["id_student"]

    def __unicode__(self):
        return str(self.id_student)


class Score(models.Model):
    # id primary key
    exercise = models.ForeignKey(Exercise)
    student = models.ForeignKey(Student)  # Does not show in Migrations
    date = models.DateTimeField()
    score = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return self.student, self.date, self.exercise
