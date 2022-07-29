from django.shortcuts import render
from .forms import Student_Registration


def shoeformsdata(request):
    FM = Student_Registration()
    FM.order_fields(field_order= ['email','name'])
    return render(request,'enroll/registrations.html',{'forms':FM})
