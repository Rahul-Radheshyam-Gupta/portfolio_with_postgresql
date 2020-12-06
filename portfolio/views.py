from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Job
import json
def index(request):
    return HttpResponse("Yes Called successfully")

def job(request):
    if request.method == "GET":
        jobs = Job.objects.all()
        result = []
        for job in jobs:
            result.append({
                'company' : job.company,
                'description' : job.description
            })
        return render(request,'portfolio/index.html',{'jobs':result})