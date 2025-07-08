from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('employee/', EmployeeList.as_view(), name='employee-get'),
    path('employee/delete/', DeleteEmployee.as_view(), name='employee-delete'),
    path('', views.pie_show, name='analysis')
]