from django.contrib import admin
from .models import Exercise, Workout, Equipment
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(Exercise)
class ExerciseAdmin(ImportExportModelAdmin):
    pass


@admin.register(Workout)
class WorkoutAdmin(ImportExportModelAdmin):
    pass


@admin.register(Equipment)
class EquipmentsAdmin(ImportExportModelAdmin):
    pass