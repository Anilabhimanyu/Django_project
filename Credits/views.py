from django.views import View
from django.http import JsonResponse
import json
from .models import CreditsTableList

class CreditsListView(View):
    def get(self, request):
        credits = CreditsTableList.objects.all()
        print(credits)
        data = [{'course_id': credit.courseId, 'issue_date': credit.issueDate} for credit in credits]
        return JsonResponse(data, safe=False)
        # return JsonResponse(credits)

    def post(self, request):
        data = json.loads(request.body)
        course_id = data.get("course_id")
        issue_date = data.get("issue_date")
        credits = CreditsTableList.objects.create(courseId=course_id, issueDate=issue_date)
        credits.save()

        return JsonResponse({'message': 'Credits created successfully'})
        
        
        
        
        