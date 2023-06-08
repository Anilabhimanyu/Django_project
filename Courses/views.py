from django.shortcuts import render
from django.http import JsonResponse
from Courses.models import Course_List
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import csv

import json

def courseListView(request):
    courses = Course_List.objects.all()
    course_list = []
    for course in courses:
        course_data = {
            'title': course.title,
            'description': course.description,
            'prerequisites': course.prerequisites,
            'author': course.author
        }
        course_list.append(course_data)

    with open('file.csv', 'w', newline='') as csvfile:
            fieldnames = course_list[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(course_list) 
    return JsonResponse({'message': 'CSV file created successfully'})

@csrf_exempt
def courseListInsert(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        description = data.get('description')
        prerequisites = data.get('prerequisites')
        author = data.get('author')

        course = Course_List(title=title, description=description, prerequisites=prerequisites, author=author)
        course.save()

        response = {'message': 'Course created successfully'}
        return JsonResponse(response, status=201)

    response = {'error': 'Invalid request method'}
    return JsonResponse(response, status=400)

@csrf_exempt
def courseListDelete(request, course_id):
    try:
        course = Course_List.objects.get(id=course_id)
    except Course_List.DoesNotExist:
        response = {'error': 'Course not found'}
        return JsonResponse(response, status=404)

    if request.method == 'DELETE':  
        course.delete()

        response = {'message': 'Course deleted successfully'}
        return JsonResponse(response)

    response = {'error': 'Invalid request method'}
    return JsonResponse(response, status=400)

@csrf_exempt
def courseListUpdate(request, course_id):
    try:
        course = Course_List.objects.get(id=course_id)
    except Course_List.DoesNotExist:
        response = {'error': 'Course not found'}
        return JsonResponse(response, status=404)

    if request.method == 'PUT':
        data = json.loads(request.body)
        # title = request.POST.get('title')
        # description = request.POST.get('description')
        # prerequisites = request.POST.get('prerequisites')
        # author = request.POST.get('author')
        title = data.get('title')
        description = data.get('description')
        prerequisites = data.get('prerequisites')
        author = data.get('author')

        course.title = title
        course.description = description
        course.prerequisites = prerequisites
        course.author = author
        course.save()

        response = {'message': 'Course updated successfully'}
        return JsonResponse(response)

    response = {'error': 'Invalid request method'}
    return JsonResponse(response, status=400)

@csrf_exempt
def save_course_data(request):
    data=Course_List.objects.all()
