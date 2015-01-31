import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoProject.settings')

import django
django.setup()

from dashboard.models import Student, Exercise, Score


def populate():

    st1 = add_student(1, 1, '101')
    st2 = add_student(2, 1, '102')
    st3 = add_student(3, 2, '201')
    st4 = add_student(4, 2, '201')

    ex1 = add_exercise(1, 1, 5)
    ex2 = add_exercise(1, 2, 5)
    ex3 = add_exercise(2, 1, 5)
    ex4 = add_exercise(2, 2, 5)

    add_score(st1[1], ex1, '2015-01-11 08:05:30.000', 3)
    add_score(st2, ex2, '2015-01-11 08:05:30.000', 4)
    add_score(st3, ex3, '2015-01-11 08:05:30.000', 5)
    add_score(st4, ex4, '2015-01-11 08:05:30.000', 2)

    # Print out what we have added to the user.
    print("Add complete")
    for st in Student.objects.all():
        print("{0}".format(str(st)))
        # print(str(st))
    for ex in Exercise.objects.all():
        # print("- {0}".format(str(ex)))
        print(str(ex))
    # for sc in Score.objects.all():
    #     print("- {0}.format(str(sc)))


def add_student(student, school, iclass):
    st = Student.objects.get_or_create(id_student=student, id_school=school, id_class=iclass)[0]
    return st


def add_exercise(app, exercise, maxsc):
    ex = Exercise.objects.get_or_create(id_app=app, id_exercise=exercise, scoremax_possible=maxsc)[0]
    return ex


def add_score(exercise, student, date, score):
    sc = Score.objects.get_or_create(exercise=ex,
                                     student=student, date=date, score=score)[0]
    return sc

# Start execution here!
if __name__ == '__main__':
    print("Starting DB population script...")
    populate()