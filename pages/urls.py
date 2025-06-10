from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('clubs/<int:club_id>/announcement/create/', views.create_announcement, name='create_announcement'),
    path('clubs/<int:club_id>/announcements/<int:announcement_id>/delete/', views.del_announcement, name='del_announcement'),
]
