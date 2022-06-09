from django.shortcuts import render

from hroom.settings import EMAIL_HOST_USER
from .forms import Subscribe
from django.core.mail import send_mail
from django_countries import countries

# Create your views here.
#DataFlair #Send Email

def subscribe(request):

    sub = Subscribe(initial={'country': 'ZA'})
    if request.method == 'POST':
        sub = Subscribe(request.POST or None, request.FILES or None)
        sub.save()
        subject = 'Welcome to The Headroom Project'
        message = 'Thank you for signing up for the Headroom Project. We will email you each time a new evolution is uploaded. Try uploading one yourself!'
        recepient = str(sub['email'].value())
        send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'subscribe/success.html', {'recepient': recepient})
    return render(request, 'subscribe/index.html', {'form':sub})