# Create your views here.

from rest_framework import permissions
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from models import Student
from serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders it's content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
        

@csrf_exempt
@api_view(['GET'])

def student_me(request):
    try:
        students = Student.objects.get(userid=request.user)
    except Student.DoesNotExist:
        return HttpResponse(status=404)
    pass
    if request.method == 'GET':
        serializer = StudentSerializer(students)

        return JSONResponse(serializer.data)