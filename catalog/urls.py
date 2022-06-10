from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from django.conf.urls import url
#from catalog import views as catalog_views
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)

urlpatterns = [
    path('', views.index, name='index'), 
    path('upload/', views.SoundUploadView.as_view(), name='upload-file'),
    path('download/', views.SoundDownloadView.as_view(), name='download-file'),
    path('seed/', views.SoundSeedView.as_view(), name='sound-seed'),      

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''

urlpatterns = [
	path('', views.index, name='index'),
    path('upload/', views.SoundUploadView.as_view(), name='upload-file'),
    path('download/', views.SoundDownloadView.as_view(), name='download-file'),
    path('seed/', views.SoundSeedView.as_view(), name='sound-seed'),    	
    path('sign-up/', views.EmailUploadView.as_view(), name='sign-up'),
    path('stem-upload/', views.StemUploadView.as_view(), name='stem-upload'),
    path('stems-download/', views.StemDownloadView.as_view(), name='stems-download'),
    path('live-seed-history', views.LiveSeedView.as_view(), name='live-seed-history'),
    path('live-download', views.LiveDownloadView.as_view(), name='live-download'),  
    path('live-upload', views.LiveUploadView.as_view(), name='live-upload'),  
    path('stem-seed-history', views.StemSeedView.as_view(), name='stem-seed-history'),
    path('acknowledgments', views.AckView.as_view(), name='acknowledgments'),
    path('acknowledgments', views.AckView.as_view(), name='acknowledgments'),    
    path('contact', views.ContactView.as_view(), name='contact'),
    path('contact-success', views.ContactSuccess.as_view(), name='contact-success'),
    path('sound-compare', views.SoundComparisonView.as_view(), name='sound-compare'),
    path('stems-compare', views.StemComparisonView.as_view(), name='stems-compare'),
    path('live-compare', views.LiveComparisonView.as_view(), name='live-compare'),
    path('sound-compare-two', views.SoundComparisonTwoView.as_view(), name='sound-compare-two'),
    path('stems-compare-two', views.StemComparisonTwoView.as_view(), name='stems-compare-two'),
    path('live-compare-two', views.LiveComparisonTwoView.as_view(), name='live-compare-two'),
    path('live-download-cont', views.Live2DownloadView.as_view(), name='live-download-cont'),
    path('live-download-cont-two', views.LiveDownloadViewTwo.as_view(), name='live-download-cont-two'),    
    path('tour', views.TourView.as_view(), name='tour'),
    path('signed-url/', views.SignedURLView.as_view(), name='signed-url'),
    path('live-upload-cont', views.LiveUploadViewTwo.as_view(), name='live-upload-cont'),               
    url(r'^signup/$', catalog_views.signup, name='signup'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''