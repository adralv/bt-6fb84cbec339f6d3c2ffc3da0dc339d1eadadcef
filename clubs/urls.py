from django.urls import path
from . import views

urlpatterns = [
    path('',views.club_list, name='club_list'),
    path('join/<int:club_id>/',views.join_club, name="join_club"),
    path('leave/<int:club_id>/',views.leave_club, name="leave_club"),
    path('<int:club_id>', views.club_details, name='club_details'),
    ]
