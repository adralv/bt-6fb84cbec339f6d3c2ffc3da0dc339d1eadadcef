from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from clubs.models import Club
from users.models import UserProfile
from event.models import Event
from Announcements.models import Announcements
from django.utils.timezone import now
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from django.http import JsonResponse, HttpResponseForbidden

# Create your views here.
@login_required
def index(request):
    user = request.user
    try:
        user_profile = UserProfile.objects.get(user=user)
        clubs = Club.objects.filter(club_members=user)
        events = Event.objects.all()
        valid_events = [
            event for event in events
            if (event.public_event or event.club in clubs) and event.end >= now()
        ]
        total_events = [event for event in events if (event.public_event or event.club in clubs)]
    except UserProfile.DoesNotExist:
        user_profile = None  
        clubs = Club.objects.none()  # No clubs
        valid_events = Event.objects.filter(public_event=True, end__gte=now())  # Only public future events

    context = {
        'user': user,
        'clubs': clubs,
        'user_profile': user_profile,
        'events': valid_events,
        'total_events':total_events
    }
    
    return render(request, 'index.html', context)

@login_required
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject', 'No Subject')
        message = request.POST.get('message')
        user_email = request.user.email  # Automatically use user's email

        full_message = f"""
        You have received a new contact form submission:

        From: {name}
        Email: {user_email}

        Message:
        {message}
        """

        try:
            send_mail(
                subject=subject,
                message=full_message,
                from_email=user_email,
                recipient_list=['ravpatw26@bergen.org'],
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')  # Make sure this name matches your URL
        except Exception as e:
            messages.error(request, f'Error sending email: {e}')

    return render(request, 'contact.html')

def create_announcement(request, club_id):
    club = Club.objects.get( id=club_id)
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        date = datetime.now()
        location = club.room_number
        user=request.user
        Announcements.objects.create(
            club=club,
            title=title,
            description=description,
            date=date,
            location=location,
            user=user
        )
        return redirect('club_details', club_id=club.id)  # Redirect back to the club page

    return render(request, 'announcement.html', {'club': club})

def del_announcement(request, club_id, announcement_id):
    if request.method == 'POST':
        try:
            announcement = Announcements.objects.get(id=announcement_id, club_id=club_id)
            if request.user != announcement.user:
                return HttpResponseForbidden("You are not allowed to delete this announcement.")

            announcement.delete()
            return JsonResponse({'status': 'success'})
        except Announcements.DoesNotExist:
            return JsonResponse({'error': 'Announcement not found'}, status=404)
    return JsonResponse({'error': 'Invalid request method'}, status=400)