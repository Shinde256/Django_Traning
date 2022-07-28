from django.shortcuts import render

def Courses_Details(request):
    name = 'Amol Aptil'
    job = 'AWS Consultant'
    company = 'Cognizant India Pvt Ltd'
    Django_details = {'nm':name,'jb':job, 'cmpn':company}
    return render(request,'course.html',context=Django_details)
