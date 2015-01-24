from django.shortcuts import render
from dashboard.models import Scores
import csv
from .forms import UploadFileForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext


def index(request):
    context = RequestContext(request)
    context_dict = {'message': 'Upload!', 'anothermessage': 'Testing!'}
    return render_to_response('dashboard/index.html', context_dict, context)


def scores(request):
    students = Scores.objects.order_by("-date")
    exercises = Scores.objects.order_by("-date")
    scores = Scores.objects.order_by("-date")
    return render(request, 'dashboard/scores.html', {"students": students, "exercises": exercises, "scores": scores})


def handle_csv_upload(request):
    if request.method == 'POST':
        my_file = request.FILES['upload']
        with open(my_file, 'rU', encoding='utf-8') as csvfile:
            # sniff to find the format
            fileDialect = csv.Sniffer().sniff(csvfile.read(1024))
            csvfile.seek(0)
            # read the CSV file into a dictionary
            dictReader = csv.DictReader(csvfile, dialect=fileDialect)
            for row in dictReader:
                # do your processing here
                yield(row)


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_csv_upload(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render_to_response('dashboard/upload.html', {'form': form})