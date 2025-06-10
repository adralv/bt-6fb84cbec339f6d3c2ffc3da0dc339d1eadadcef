from django.shortcuts import render

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# @login_required
# def contact_view(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         subject = request.POST.get('subject', 'No subject')
#         message = request.POST.get('message')

#         full_message = f"Message from {name} <{email}>:\n\n{message}"

#         try:
#             send_mail(
#                 subject,
#                 full_message,
#                 email,  # from
#                 ['darknoob561@gmail.com'],  # to
#                 fail_silently=False,
#             )
#             messages.success(request, "Your message was sent successfully.")
#         except Exception as e:
#             messages.error(request, f"Error sending message: {e}")

#         return redirect('contact')  # Or wherever you want to redirect

#     return render(request, 'contact.html')
