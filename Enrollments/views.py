from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import StudEnrollments
from django.db import connection
from EDUFRENT.settings import DATABASES
import mysql.connector
from rest_framework.response import Response

from django.http import JsonResponse
from django.db import connection


# def get_database_connection():
#     config = {
#         'user': DATABASES['default']['USER'],
#         'password': DATABASES['default']['PASSWORD'],
#         'host': DATABASES['default']['HOST'],
#         'port': DATABASES['default']['PORT'],
#         'database': DATABASES['default']['NAME'],
#         'raise_on_warnings': True,
#     }
#     return mysql.connector.connect(**config)

@csrf_exempt
def student_add(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        age = data.get('age')
        email = data.get('email')
        course = data.get('course')
        
        with connection.cursor() as cursor:
            query = "INSERT INTO Enrollments_StudEnrollments (name, age, email, course) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, [name, age, email, course])
            cursor.close()
            # connection.close()

        response = {'message': 'Student enrollment created successfully'}
        return JsonResponse(response, status=201)

    response = {'error': 'Invalid request method'}
    return JsonResponse(response, status=400)





def student_view(request):
    print('hi==================')
    if request.method == 'GET':
        cursor = connection.cursor()
        print(1)
        cursor.execute("SELECT * FROM Enrollments_StudEnrollments")
        print(2)
        enrollments = cursor.fetchall()
        print(3)

        enrollment_list = []
        for enrollment in enrollments:
            enrollment_dict = {
                'name': enrollment[0],
                'age': enrollment[1],
                'email': enrollment[2],
                'course': enrollment[3]
            }
            print(enrollment_dict)
            # enrollment_list.append({"0":enrollment_dict})

        response = {'enrollments': enrollment_list}
        return JsonResponse(response)

    response = {'error': 'Invalid request method'}
    return JsonResponse(response, status=400)


# def student_view(request):
#     if request.method == 'GET':
#         cursor=connection.cursor()
#         cursor.execute("SELECT * FROM Enrollments_StudEnrollments")
#         op=cursor.fetchall()
#         return Response(op)
        # connection = get_database_connection()
        # with connection.cursor() as cursor:
        #     query = "SELECT * FROM StudEnrollments"
        #     cursor.execute(query)
        #     enrollments = cursor.fetchall()
        #     cursor.close()
        #     connection.close()

        # enrollment_list = [
        #     {'name': enrollment[0], 'age': enrollment[1], 'email': enrollment[2], 'course': enrollment[3]}
        #     for enrollment in enrollments
        # ]

        # response = {'enrollments': enrollment_list}
        # return JsonResponse(response)

    # response = {'error': 'Invalid request method'}
    # return JsonResponse(response, status=400)



# @csrf_exempt
# def student_update(request, enrollment_id):
#     try:
#         enrollment = get_enrollment_by_id(enrollment_id)
#         if not enrollment:
#             raise StudEnrollment.DoesNotExist
#     except StudEnrollment.DoesNotExist:
#         response = {'error': 'Student enrollment not found'}
#         return JsonResponse(response, status=404)

#     if request.method == 'PUT':
#         data = json.loads(request.body)
#         name = data.get('name')
#         age = data.get('age')
#         email = data.get('email')
#         course = data.get('course')

#         with connection.cursor() as cursor:
#             query = "UPDATE student_enrollment SET name = %s, age = %s, email = %s, course = %s WHERE id = %s"
#             cursor.execute(query, [name, age, email, course, enrollment_id])

#         response = {'message': 'Student enrollment updated successfully'}
#         return JsonResponse(response)

#     response = {'error': 'Invalid request method'}
#     return JsonResponse(response, status=400)

def get_enrollment_by_email(email):
    connection=get_database_connection()
    with connection.cursor() as cursor:
        query = "SELECT * FROM Enrollments_StudEnrollments WHERE email = %s"
        cursor.execute(query, [email])
        enrollment = cursor.fetchone()
        cursor.close()
        connection.close()
    return enrollment

@csrf_exempt
def student_update(request, email):
    try:
        enrollment = get_enrollment_by_email(email)
        if not enrollment:
            raise StudEnrollment.DoesNotExist
    except StudEnrollment.DoesNotExist:
        response = {'error': 'Student enrollment not found'}
        return JsonResponse(response, status=404)

    if request.method == 'PUT':
        data = json.loads(request.body)
        course = data.get('course')
        connection=get_database_connection()
        with connection.cursor() as cursor:
            query = "UPDATE Enrollments_StudEnrollments SET course = %s WHERE email = %s"
            cursor.execute(query, [course, email])
            cursor.close()
            connection.close()
        response = {'message': 'Student enrollment updated successfully'}
        return JsonResponse(response)

    response = {'error': 'Invalid request method'}
    return JsonResponse(response, status=400)



@csrf_exempt
def student_delete(request, email):
    try:
        enrollment = get_enrollment_by_email(email)
        if not enrollment:
            raise StudEnrollment.DoesNotExist
    except StudEnrollment.DoesNotExist:
        response = {'error': 'Student enrollment not found'}
        return JsonResponse(response, status=404)

    if request.method == 'DELETE':
        connection=get_database_connection()
        with connection.cursor() as cursor:
            query = "DELETE FROM Enrollments_StudEnrollments WHERE email = %s"
            cursor.execute(query, [email])
            cursor.close()
            connection.close()

        response = {'message': 'Student enrollment deleted successfully'}
        return JsonResponse(response)

    response = {'error': 'Invalid request method'}
    return JsonResponse(response, status=400)
