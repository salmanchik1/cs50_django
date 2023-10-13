from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    timestamp = datetime.datetime.now()
    it_is_new_year = (timestamp.day == 1 and timestamp.month == 1)
    return render(request, 'newyear/index.html', {'it_is_new_year': it_is_new_year})
