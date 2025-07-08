from django.shortcuts import render
from .models import Employee
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count

# Create your views here.
class EmployeeList(APIView):
    def get(self, request):
        try:
            employee = Employee.objects.get(id=request.data["id"])
            return Response({'Message': 'Requested Employee Details', 'Employee Details': employee})
        except:
            employees = Employee.objects.all().values()
            return Response({'Message': 'List of Employees', 'Employees list': employees})

    
    def post(self, request):
        try:
            employee = Employee.objects.create(name=request.data['name'],
                                    department=request.data['department'])
            employee_details = Employee.objects.all().filter(id=employee.id).values()
            return Response({'Message': 'New Employee Added', 'Employee Details': employee_details})
        
        except:
            return Response({'Message': 'Employee ID is taken.'})
        
    def put(self, request):
        try:
            employee = Employee.objects.get(id=request.data["id"])
            employee.name = request.data["name"]
            employee.department = request.data['department']
            employee.save()
            employee_details = Employee.objects.all().filter(id=request.data['id']).values()
            return Response({'Message': 'Details Updated', 'Employee Details': employee_details})
        except:
            return Response({'Message': 'Employee does not exist'})
        
    def delete(self, request):
        try:
            employee = Employee.objects.get(id=request.data["id"])
            employee.delete()
            return Response({"Message": "Successfully Deleted"})
        
        except:
            return Response({"Message": "Enter Valid Employee ID to delete."})
            

class DeleteEmployee(APIView):
    def delete(self, request):
        Employee.objects.all().delete()
        return Response({"All records deleted"})
    

def pie_show(request):
    data = (
        Employee.objects.values('department')
        .annotate(count=Count('department'))
        .order_by()
    )
    labels = [item['department'] for item in data]
    counts = [item['count'] for item in data]

    return render(request, 'pie_chart.html', {
        'labels': labels,
        'counts': counts
    })