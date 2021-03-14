import InputController as InputController
from InputController import displayInput
import ScheduleController as ScheduleController
from django import get_version
import django

print("Test")

displayInput()
print(django.get_version())