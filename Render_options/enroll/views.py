from django.shortcuts import render
from .forms import Student_Registration


def shoeformsdata(request):
    FM = Student_Registration()
    return render(request,'enroll/registrations.html',{'forms':FM})
