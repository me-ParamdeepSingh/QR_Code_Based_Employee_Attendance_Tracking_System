from django.urls import path
from . import views
urlpatterns = [
    path('my-attendance/', views.my_attendance, name='my_attendance'),
    path('all-attendance/', views.all_attendance, name='all_attendance'),
    path('scan-qr/', views.scan_qr, name='scan_qr'),
    path("mark/", views.mark_attendance, name="mark_attendance"),
    path("report/", views.report, name="report"),
    path("export-report/", views.report, name="export_report"),
]
