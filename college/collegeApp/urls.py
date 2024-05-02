from django.urls import path
from .views import *
urlpatterns=[
    path('Home/',index),
    path('busregister/',busRegister),
    path('mail/',mailRegister),
    path('morning/',busAttendanceMorning),
    path('evening/',busAttendanceEvening),
    path('display/',dispaly),
    path('maildisplay/',maildis)

    # path('cam/',Home)
]