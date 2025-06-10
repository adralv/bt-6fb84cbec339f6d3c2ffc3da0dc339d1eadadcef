from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Club
from Announcements.models import Announcements
from django.contrib.auth.models import User
from event.models import Event
from taggit.models import Tag
from django.utils.timezone import now
# Create your views here.
@login_required
def club_list(request):
    clubs = Club.objects.order_by('club_name')
    keywords = request.GET.get('keywords', '')
    tags = request.GET.get('tag', '')
    page = request.GET.get('page', 1)

    if keywords:
        clubs = clubs.filter(club_name__icontains=keywords)

    if tags and tags != 'All':
        clubs = clubs.filter(tags__name__iexact=tags)
        
    paginator = Paginator(clubs,8)
    page = request.GET.get('page')
    paged_clubs = paginator.get_page(page)
    context = {
        'clubs' : paged_clubs,
        'tags': Tag.objects.all(),
    }
    return render(request, 'club_list.html', context)

@login_required
def club_details(request,club_id):
    club= Club.objects.get(id=club_id)
    events= Event.objects.filter(club_id=club_id)
    announcements=Announcements.objects.filter(club=club).order_by('date').reverse()
    valid_events = [
        event for event in events
        if event.end >= now()
    ]
    context={
        'club':club,
        'announcements':announcements,
        'events':valid_events
    }
    return render(request, 'club_detail.html',context)

@login_required
def join_club(request, club_id):
    club= Club.objects.get(id=club_id)
    club.club_members.add(request.user)
    return redirect('club_details',club_id=club_id)
@login_required
def leave_club(request, club_id):
    club= Club.objects.get(id=club_id)
    club.club_members.remove(request.user)
    return redirect('club_details',club_id=club_id)
    
    
