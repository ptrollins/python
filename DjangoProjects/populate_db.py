import os


def populate():

    add_student(1, 1, '101')
    add_student(2, 1, '102')
    add_student(3, 2, '201')
    add_student(4, 2, '201')

    add_exercise(1, 1, 5)
    add_exercise(1, 2, 5)
    add_exercise(2, 1, 5)
    add_exercise(2, 2, 5)

    add_score(1, 1, 'dim jan 11 08:05:30 GMT 2015', 3)
    add_score(2, 1, 'dim jan 11 08:05:30 GMT 2015', 4)
    add_score(3, 2, 'dim jan 11 08:05:30 GMT 2015', 5)
    add_score(4, 2, 'dim jan 11 08:05:30 GMT 2015', 2)

    # Print out what we have added to the user.
    for st in Student.objects.all():
        print("- {0} - {1}".format(str(st)))
    for ex in Exercise.objects.all():
        print("- {0} - {1}".format(str(ex)))
    for sc in Score.objects.all():
        print("- {0} - {1}".format(str(sc)))


def add_student(student, school, iclass):
    st = Student.objects.get_or_create(id_student=student, id_school=school, id_class=iclass)[0]
    return st


def add_exercise(app, exercise, max):
    ex = Exercise.objects.get_or_create(id_app=app, id_exercise=exercise, scoremax_possible=max)[0]
    return ex


def add_score(exercise, student, date, score):
    sc = Score.objects.get_or_create(exercise=exercise, student=student, date=date, score=score)[0]
    return sc

# Start execution here!
if __name__ == '__main__':
    print("Starting DB population script...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoProject.settings')
    from dashboard.models import Exercise, Score, Student
    populate()