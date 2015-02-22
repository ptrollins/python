from dashboard.models import Score, Exercise, Student  # to use models
import csv  # for CSV parser
import sqlite3  # for DB
from .forms import UploadFileForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext
from django.core.context_processors import csrf  # For form POST security CSRF token
from django.contrib import auth  #for authentication
from io import TextIOWrapper  #
from django.shortcuts import render


def index(request):
    context = RequestContext(request)
    context_dict = {'message': 'Login'}
    return render_to_response('dashboard/index.html', context_dict, context)


def dashboard(request):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    # Query the database for a list of ALL students currently stored.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    students_list = Student.objects.order_by("id_student")
    exercises_list = Exercise.objects.order_by("id_app")
    scores_list = Score.objects.order_by("date")
    context_dict = {"student": students_list, "exercise": exercises_list, "score": scores_list}

    return render_to_response('dashboard/dashboard.html', context_dict, context)


def usage(request):
    context = RequestContext(request)
    score_list = [s.score for s in Score.objects.all()]
    context_dict = {"score": score_list}
    return render_to_response('dashboard/usage.html', context_dict, context)


def scores(request):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    # Query the database for a list of ALL students currently stored.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    scores_list = Score.objects.order_by("exercise__id_exercise")
    # score_list = [s.score for s in Score.objects.all()]
    # {'score_list': [student_score.score for student_score in Score.objects.get(student__id=3)]}
    context_dict = {"score": scores_list}

    # Render the response and send it back!
    return render_to_response('dashboard/scores.html', context_dict, context)


def classes(request):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    # Query the database for a list of ALL students currently stored.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    students_list = Student.objects.order_by("id_student")
    exercises_list = Exercise.objects.order_by("id_app")
    scores_list = Score.objects.all()
    context_dict = {"student": students_list, "exercise": exercises_list, "score": scores_list}
    return render_to_response('dashboard/class.html', context_dict, context)


def upload_file(request):
    context = RequestContext(request)
    args = {}
    args.update(csrf(request))
    #  When button is clicked method is POST so file is uploaded with request.FILES
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        args['form'] = form
        if form.is_valid():
            # File is formatted Byte so is wrapped as utf-8 and passed to handler
            handle_csv_upload(TextIOWrapper(request.FILES['file'].file, encoding='utf-8'))
            # After handler inserts into database, redirect calls page to display data
            return HttpResponseRedirect('display')
    # First time on the page method is GET so form is rendered on upload.html
    else:
        form = UploadFileForm()
        args['form'] = form
    return render_to_response('dashboard/upload.html', args, context)


def handle_csv_upload(csvfile):
    reader = csv.reader(csvfile)  # read the CSV file into a list of strings
    connection = sqlite3.connect('dashboard.db')  # Create the database connection and cursor

    for row in reader:  # for each row from the CSV format the data to correct data type and insert into database
        # 0 = id_app, 1 = date, 2 = id_student, 3 = id_school, 4 = id_class,
        # 5 = id_exercise, 6 = score, 7 = scoremax_possible
        formatted_date = format_date(row[1])
        with connection:
            Exercise.objects.get_or_create(id_app=int(row[0]), id_exercise=int(row[5]),
                                                scoremax_possible=int(row[7]))
            # Stores object to use as foreign key in Score Insert
            exer = Exercise.objects.get(id_app=int(row[0]), id_exercise=int(row[5]))

            Student.objects.get_or_create(id_student=int(row[2]), id_school=int(row[3]), id_class=row[4])
            # Stores primary key to use as foreign key in Score Insert
            stud = Student.objects.get(id_student=int(row[2]))

            Score.objects.get_or_create(date=formatted_date, score=int(row[6]), student=stud, exercise=exer)

    # Close the csv file, commit changes, and close the connection
    csvfile.close()
    connection.commit()
    connection.close()


def format_date(date):
    # Converts cvs date 'dim jan 11 08:05:30 GMT 2015' to SQLite date format '2015-01-11 08:05:30.000'
    upper_date = date.upper()
    date_list = upper_date.split()
    month = monthToNum(date_list[1])
    formatted_date = '{}-{}-{} {}.000'.format(date_list[5], month, date_list[2], date_list[3])
    return formatted_date


def monthToNum(date):  # Def to convert month abbreviation to a number

    return{
        'JAN': '01',  # For English
        'FEB': '02',
        'MAR': '03',
        'APR': '04',
        'MAY': '05',
        'JUN': '06',
        'JUL': '07',
        'AUG': '08',
        'SEP': '09',
        'OCT': '10',
        'NOV': '11',
        'DEC': '12',
        'FEV': '02',  # For French
        'AVR': '04',
        'MAI': '05',
        'AOU': '08',
    }[date]


# authentication
def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login', c)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        HttpResponseRedirect('accounts/loggedin.html')
    else:
        HttpResponseRedirect('accounts/invalid.html')


def loggedin(request):
    return render_to_response('loggedin.html',
        {'full_name': request.user.username})


def invalid_login(request):
    return render_to_response('invalid_login.html')


def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')



