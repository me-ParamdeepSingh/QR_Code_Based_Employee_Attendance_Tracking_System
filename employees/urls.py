from django.urls import path
from . import views
urlpatterns = [
    path('employee-list/', views.employee_list, name='employee_list'),
    path('add-employee/', views.add_employee, name='add_employee'),
    path('employee-detail/', views.employee_detail, name='employee_detail'),
    path('edit-employee/', views.edit_employee, name='edit_employee'),
]
