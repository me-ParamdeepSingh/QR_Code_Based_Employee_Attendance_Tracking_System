from django.shortcuts import render

# Create your views here.
def employee_list(request):
    return render(request, 'employees/employee_list.html')

def add_employee(request):
    return render(request, 'employees/add_employee.html')

def employee_detail (request):
    return render(request, 'employees/employee_detail.html')

def edit_employee (request):
    return render(request, 'employees/edit_employee.html')