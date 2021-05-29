from rest_framework import serializers
from .models import Workout, Exercise, Equipment


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['name', 'description', 'muscle_group', 'muscle_worked', 'equipment', 'video_path', 'image_path',
                  'workout']
        read_only_fields = fields
        depth = 2


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['name', 'image_path']
        read_only_fields = fields


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ['name', 'image_path']
        read_only_fields = fields
