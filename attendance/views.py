from django.shortcuts import render

# Create your views here.
def my_attendance(request):
    return render(request,'attendance/my_attendance.html')

def all_attendance(request):
    return render(request,'attendance/all_attendance.html')

def scan_qr(request):
    return render(request,'attendance/scan_qr.html')

def mark_attendance(request):
    return render(request,'attendance/scan_qr.html')

def report(request):
    return render(request,'attendance/report.html')
