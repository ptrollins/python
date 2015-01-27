from dashboard.models import Score, Exercise, Student  # to use models
import csv  # for CSV parser
import sqlite3  # for DB
from .forms import UploadFileForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response, RequestContext


def index(request):
    context = RequestContext(request)
    context_dict = {'message': 'Upload!', 'anothermessage': 'Testing!'}
    return render_to_response('dashboard/index.html', context_dict, context)


def scores(request):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    # Query the database for a list of ALL students currently stored.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    score_list = Student.objects.order_by("id_student")
    context_dict = {"student": score_list}

    # Render the response and send it back!
    return render_to_response('dashboard/scores.html', context_dict, context)
    # return render(request, 'dashboard/scores.html', {"student": students, "exercise": exercises, "score": score})


def handle_csv_upload(request):
    # Create the database connection
    connection = sqlite3.connect('')
    cursor = connection.cursor()

    if request.method == 'POST':
        my_file = request.FILES['upload']
        with open(my_file, 'rU', encoding='utf-8') as csvfile:
            # sniff to find the format
            fileDialect = csv.Sniffer().sniff(csvfile.read(1024))
            csvfile.seek(0)
            # read the CSV file into a dictionary
            dictReader = csv.DictReader(csvfile, dialect=fileDialect)
            for row in dictReader:
                cursor.execute('INSERT INTO Exercise VALUES (?,?,?)', row)
                cursor.execute('INSERT INTO Student VALUES (?,?,?)', row)
                cursor.execute('INSERT INTO Score VALUES (?,?,?)', row)
                # yield(row)

    # Close the csv file, commit changes, and close the connection
    csvfile.close()
    connection.commit()
    connection.close()



def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_csv_upload(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render_to_response('dashboard/upload.html', {'form': form})