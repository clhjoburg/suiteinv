from django.shortcuts import render
#from catalog.models import sound, live, livelarge, stem, emaillist, contact, tourinput, cameronbio 
from django_countries import countries
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import os
from django.core.files import File
from . import forms
from hroom.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
#from catalog.forms import Upload, StemUpload, LiveUpload, ContactUpload
from django.views.generic.edit import FormView
from django.template import RequestContext
import json
import boto3
from django.conf import settings
from django.http import JsonResponse

'''
class SignedURLView(generic.View):
    def post(self, request, *args, **kwargs):
        session = boto3.session.Session()
        client = session.client(
            "s3",
            region_name=settings.AWS_S3_REGION_NAME,
            endpoint_url=settings.AWS_S3_ENDPOINT_URL,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        )

        url = client.generate_presigned_url(
            ClientMethod="put_object",
            Params={
                "Bucket": "hroom",
                "Key": f"uploads/{json.loads(request.body)['fileName']}",
            },
            ExpiresIn=300,
        )
        return JsonResponse({"url": url})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/subscribe')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def index(request):
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
    #return HttpResponseRedirect('/login')
  

class SoundUploadView(LoginRequiredMixin, FormView):
    model = sound
    template_name = 'upload.html'
    form_class = Upload
    success_url = reverse_lazy('sound-seed')

    def form_valid(self, form):
        upload_form = form.save(commit=False)
        upload_form.user = self.request.user
        upload_form.save()
        
        return super().form_valid(form)

    
class SoundDownloadView(generic.ListView):

    model = sound
    fields = ['sound_file']
    template_name = 'download.html'

    def get_queryset(self):
        return sound.objects.first()

class SoundComparisonView(generic.ListView):

    model = sound
    fields = ['sound_file']
    first_element = sound.objects.first()
    last_element = sound.objects.last()
    template_name = 'sound-compare.html'

    def get_queryset(self):
        return sound.objects    

class SoundComparisonTwoView(generic.ListView):

    model = sound
    fields = ['sound_file']
    first_element = sound.objects.first()
    last_element = sound.objects.last()
    template_name = 'sound-compare-two.html'

    def get_queryset(self):
        return sound.objects

class SoundSeedView(generic.ListView):

    model = sound
    fields = ['sound_file']
    template_name = 'seed_history.html'
    paginate_by = 6

class StemUploadView(LoginRequiredMixin, FormView):
    model = stem
    template_name = 'stem-upload.html'
    form_class = StemUpload
    success_url = reverse_lazy('stem-seed-history')

    def form_valid(self, form):
        upload_form = form.save(commit=False)
        upload_form.user = self.request.user
        upload_form.save()

        return super().form_valid(form)    

class StemDownloadView(generic.ListView):

    model = stem
    fields = '__all__'
    template_name = 'stems-download.html'

    def get_queryset(self):
        return stem.objects.first()

class StemComparisonView(generic.ListView):

    model = stem
    fields = ['mixed_render']
    first_element = stem.objects.first()
    last_element = stem.objects.last()
    template_name = 'stems-compare.html'

    def get_queryset(self):
        return stem.objects  

class StemComparisonTwoView(generic.ListView):

    model = stem
    fields = ['mixed_render']
    first_element = stem.objects.first()
    last_element = stem.objects.last()
    template_name = 'stems-compare-two.html'

    def get_queryset(self):
        return stem.objects         

class LiveUploadView(LoginRequiredMixin, FormView):
    model = live
    template_name = 'live-upload.html'
    form_class = LiveUpload
    success_url = reverse_lazy('live-seed-history')

    def form_valid(self, form):
        upload_form = form.save(commit=False)
        upload_form.user = self.request.user
        upload_form.save()

        return super().form_valid(form)                 

class LiveUploadViewTwo(generic.CreateView):
    template_name = "live-upload-cont.html"
    model = livelarge
    fields = ['file']

    def get_success_url(self):
        return reverse("live-seed-history")

    def get_context_data(self, **kwargs):
        context = super(LiveUploadViewTwo, self).get_context_data(**kwargs)
        context.update({
            "uploads": livelarge.objects.all()
        })
        return context

class LiveDownloadView(generic.ListView):

    model = live
    fields = '__all__'
    template_name = 'live-download.html'

    def get_queryset(self):
        return live.objects.first() 

class LiveDownloadViewTwo(generic.ListView):

    model = livelarge
    fields = '__all__'
    template_name = 'live-download-cont-two.html'

    def get_queryset(self):
        return livelarge.objects.first()             

class LiveSeedView(generic.ListView):

    model = live
    fields = '__all__'
    template_name = 'live-seed-history.html'

class LiveComparisonView(generic.ListView):

    model = live
    fields = ['live_render']
    first_element = live.objects.first()
    last_element = live.objects.last()
    template_name = 'live-compare.html'

    def get_queryset(self):
        return live.objects     

class LiveComparisonTwoView(generic.ListView):

    model = live
    fields = ['live_render']
    first_element = live.objects.first()
    last_element = live.objects.last()
    template_name = 'live-compare-two.html'

    def get_queryset(self):
        return live.objects                          

class StemSeedView(generic.ListView):

    model = stem
    fields = 'mixed_render'
    template_name = 'stem-seed-history.html'
    paginate_by = 6

class Live2DownloadView(generic.ListView):

    model = live
    fields = '__all__'
    template_name = 'live-download-cont.html'

    def get_queryset(self):
        return live.objects.first()

class EmailUploadView(generic.CreateView):

    model = emaillist
    fields = ['email', 'country']
    template_name = 'sign-up.html'

    def subscribe(request):
        subject = 'Welcome to the Headroom Project'
        message = 'Thank you for signing-up with the Headroom Project'
        recepient = str(['email'].value())
        send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'subscribe/success.html', {'recepient': recepient})
        return render(request, 'sign-up.html', {'form':form})   

class AckView(generic.ListView):

    model = sound
    template_name = 'acknowledgments.html'    

class ContactSuccess(generic.ListView):
    model = contact
    template_name = 'contact-success.html'

class ContactView(generic.FormView):

    model = contact
    template_name = 'contact.html'
    form_class = ContactUpload
    success_url = reverse_lazy('contact-success')

    def form_valid(self, form):
        upload_form = form.save(commit=False)
        upload_form.save()
        subject = 'Someone has contacted Headroom using the contact form'
        from_email = EMAIL_HOST_USER
        to = 'cameronlharris@gmail.com'
        msg_plain = render_to_string('../templates/email.txt')
        msg_html = render_to_string('../templates/evolemail.html')
        msg = EmailMultiAlternatives(subject, msg_plain, from_email, [to])
        msg.attach_alternative(msg_html, "text/html")
        msg.send()
        return super().form_valid(form)

class TourView(generic.ListView):

    model = tourinput
    template_name = 'tour.html'  

class camby(generic.ListView):

    model = cameronbio
    fields = '__all__'
    template_name = 'cameron.html'      
    '''