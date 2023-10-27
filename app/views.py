from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Employee
from .serializers import EmployeeSerializer

@api_view(['POST'])
def create_employee(request):
    try:
        email = request.data.get('email')
        existing_employee = Employee.objects.filter(email=email).first()
        if existing_employee:
            return Response({'message': 'Employee already exists', 'success': False}, status=status.HTTP_200_OK)

        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
           
            employee = serializer.save()

            return Response({'message': 'Employee created successfully', 'regid': employee.pk, 'success': True}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid body request', 'success': False}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'message': 'Employee creation failed', 'success': False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['PUT'])
def update_employee(request, regid):
    try:
        
        employee = Employee.objects.filter(pk=regid).first()
        if not employee:
            return Response({'message': 'No employee found with this regid', 'success': False}, status=status.HTTP_404_NOT_FOUND)

      
        serializer = EmployeeSerializer(employee, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Employee details updated successfully', 'success': True}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid body request', 'success': False}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'message': 'Employee updation failed', 'success': False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_employee_details(request):
    regid = request.GET.get('regid', None)

    if regid:
        
        employee = Employee.objects.filter(pk=regid).first()
        if employee:
            serializer = EmployeeSerializer(employee)
            return Response({'message': 'Employee details found', 'success': True, 'employees': [serializer.data]}, status=status.HTTP_200_OK)
    else:
        
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response({'message': 'Employee details found', 'success': True, 'employees': serializer.data}, status=status.HTTP_200_OK)

 
    return Response({'message': 'Employee details not found', 'success': False, 'employees': []}, status=status.HTTP_200_OK)




@api_view(['DELETE'])
def delete_employee(request):
    try:
        data = request.data

       
        if "regid" in data:
            try:
                regid = int(data["regid"])  
                
                employee = Employee.objects.filter(pk=regid).first()
                if employee:
                    
                    employee.delete()
                    return Response({'message': 'Employee deleted successfully', 'success': True}, status=status.HTTP_200_OK)
                else:
                    return Response({'message': 'No employee found with this regid', 'success': False}, status=status.HTTP_200_OK)
            except ValueError:
                return Response({'message': 'Invalid regid format', 'success': False}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Invalid body request', 'success': False}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'message': 'Employee deletion failed', 'success': False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)