import firebase_admin
from .models import Workout, Exercise, Equipment
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializers import ExerciseSerializer, WorkoutSerializer, EquipmentSerializer
from firebase_admin import auth
from firebase_admin import credentials
from django.http import JsonResponse
from rest_framework.response import Response

if not firebase_admin._apps:
    cred = credentials.Certificate('fitify-digitaldeal-firebase-adminsdk-acjin-00c888277d.json')
    default_app = firebase_admin.initialize_app(cred)


@api_view(['GET'])
def ExerciseV(request):
    if request.method == 'GET':
        params = request.GET
        uid = params['uid']
        try:
            auth.get_user(uid)
            excercises = Exercise.objects.all().order_by('name')
            serializer = ExerciseSerializer(excercises, many=True)
            return Response(serializer.data)
        except:
            return JsonResponse({"error": "User not verified"})


@api_view(['GET'])
def WorkoutV(request):
    if request.method == 'GET':
        params = request.GET
        uid = params['uid']
        try:
            auth.get_user(uid)
            workout = Workout.objects.all().order_by('name')
            serializer = WorkoutSerializer(workout, many=True)
            return Response(serializer.data)
        except:
            return JsonResponse({"error": "User not verified"})


@api_view(['GET'])
def EquipmentV(request):
    if request.method == 'GET':
        params = request.GET
        uid = params['uid']
        try:
            auth.get_user(uid)
            equipment = Equipment.objects.all().order_by('name')
            serializer = ExerciseSerializer(equipment, many=True)
            return Response(serializer.data)
        except:
            return JsonResponse({"error": "User not verified"})
