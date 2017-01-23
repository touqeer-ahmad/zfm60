from django.shortcuts import render
from myapp.models import Employee, Employeeinfo, enroll
from rest_framework import viewsets
from django.template import RequestContext
from myapp.serializers import enrollSerializer
import requests
import json

# Create your views here.
class EnrollViewSet(viewsets.ModelViewSet):
    queryset = enroll.objects.all()
    serializer_class = enrollSerializer

def home(request):
    out = ''
    currentenroll = 'off'
    
    if 'on' in request.POST:
        values = {"event": "on"}
        r = requests.put('http://127.0.0.1:8000/enroll/1/',
                        data=values, auth=('hello', 'nishil123'))
        result = r.text
        output = json.loads(result)
        out = output['event']
    if 'off' in request.POST:
        values = {"event": "off"}
        r = requests.put('http://127.0.0.1:8000/enroll/1/',
                        data=values, auth=('hello', 'nishil123'))
        result = r.text
        output = json.loads(result)
        out = output['event']
        
    r = requests.get('http://127.0.0.1:8000/enroll/1/',
                    auth=('hello', 'nishil123'))
    result = r.text
    output = json.loads(result)
    currentenroll = output['event']

    latest_employee_list = Employee.objects.all().order_by('fname')
    inter = Employee.objects.all().order_by('fname').values('fname')
    latest_employeeinfo_list = Employeeinfo.objects.filter(fname__in=inter).distinct()
    
    fppData = Employeeinfo.objects.order_by('-id')[0]
    slot= fppData.slot
    date = fppData.date
    timestamp = fppData.timestamp
    fname = fppData.fname
    lname = fppData.lname
    dpt = fppData.dpt
        
    return render(request, 'myapp/index.html', {'event' : out, 'slot' : slot, 'date' : date,'timestamp': timestamp,
                                                'fname': fname, 'lname':lname, 'dpt':dpt, 'currentenroll':currentenroll,
                                                'latest_employee_list':latest_employee_list,
                                                'latest_employeeinfo_list':latest_employeeinfo_list})

