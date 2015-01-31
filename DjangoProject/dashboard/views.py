from dashboard.models import Score, Exercise, Student  # to use models
import csv  # for CSV parser
import sqlite3  # for DB
from .forms import UploadFileForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response, RequestContext
# from django.template.defaulttags import csrf_token
from django.core.context_processors import csrf
from io import TextIOWrapper


def index(request):
    context = RequestContext(request)
    context_dict = {'message': 'Upload!', 'anothermessage': 'Testing!'}
    return render_to_response('dashboard/index.html', context_dict, context)


def display_data(request):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    # Query the database for a list of ALL students currently stored.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    students_list = Student.objects.order_by("id_student")
    exercises_list = Exercise.objects.order_by("id_app")
    scores_list = Score.objects.order_by("date")
    context_dict = {"student": students_list, "exercise": exercises_list, "score": scores_list}

    # Render the response and send it back!
    return render_to_response('dashboard/display.html', context_dict, context)


def upload_file(request):
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
    return render_to_response('dashboard/upload.html', args)


def handle_csv_upload(csvfile):
    # Create the database connection and cursor
    connection = sqlite3.connect('dashboard.db')
    cur = connection.cursor()

    reader = csv.reader(csvfile)  # read the CSV file into a list of strings
    for row in reader:  # for each row from the CSV format the data to correct data type and insert into database
        # 0 = id_app, 1 = date, 2 = id_student, 3 = id_school, 4 = id_class,
        # 5 = id_exercise, 6 = score, 7 = scoremax_possible
        formatted_date = format_date(row[1])
        with connection:
            # NULL values are for Autoincremented ID produced by SQLite
            Exercise.objects.get_or_create(id_app=int(row[0]), id_exercise=int(row[5]),
                                                scoremax_possible=int(row[7]))
            #ex.save()
            print('hi')
            # cur.execute("INSERT OR IGNORE INTO dashboard_exercise VALUES (NULL , ?, ?, ?)",
            #            (int(row[0]), int(row[5]), int(row[7])))
            # Stores primary key to use as foreign key in Score Insert
            exer_id = Exercise.objects.filter(id_app=int(row[0])).filter(id_exercise=int(row[5])).values(id)
            # exer_id = cur.execute("SELECT id FROM dashboard_exercise WHERE id_exercise=(?)", (int(row[5])))
            print("now")
            Student.objects.get_or_create(id_student=int(row[2]), id_school=int(row[3]), id_class=int(row[4]))
            #st.save()
            # cur.execute("INSERT OR IGNORE INTO dashboard_student VALUES (NULL , ?, ?, ?)",
            #            (int(row[2]), int(row[3]), row[4].upper()))
            # Stores primary key to use as foreign key in Score Insert
            stud_id = Student.objects.values(id).filter(id_student=int(row[2]))
            # stud_id = cur.execute("SELECT id FROM dashboard_student WHERE id_student=(?)", (int(row[2])))

            print(formatted_date, int(row[6]), stud_id, exer_id)
            Score.objects.get_or_create(date=formatted_date, score=int(row[6]), student=stud_id, exercise=exer_id)
            # cur.execute("INSERT OR IGNORE INTO dashboard_score VALUES (NULL , ?, ?, ?, ?)",
            #            (formatted_date, int(row[6]), stud_id, exer_id))

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