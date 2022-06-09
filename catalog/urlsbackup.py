from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from django.conf.urls import url
from catalog import views as catalog_views

urlpatterns = [
path('', views.index, name='index'),
path('download/', views.SoundDownloadView.as_view(), name='download-file'),
path('sound-compare', views.SoundComparisonView.as_view(), name='sound-compare'),
path('sound-compare-two', views.SoundComparisonTwoView.as_view(), name='sound-compare-two'),
path('seed/', views.SoundSeedView.as_view(), name='sound-seed'),
path('stems-download/', views.StemDownloadView.as_view(), name='stems-download'),
path('live-seed-history', views.LiveSeedView.as_view(), name='live-seed-history'),
path('live-download', views.LiveDownloadView.as_view(), name='live-download'),
path('stem-seed-history', views.StemSeedView.as_view(), name='stem-seed-history'),
path('stems-compare', views.StemComparisonView.as_view(), name='stems-compare'),
path('live-compare', views.LiveComparisonView.as_view(), name='live-compare'),
path('stems-compare-two', views.StemComparisonTwoView.as_view(), name='stems-compare-two'),
path('live-compare-two', views.LiveComparisonTwoView.as_view(), name='live-compare-two'),
path('live-download-cont', views.Live2DownloadView.as_view(), name='live-download-cont'),     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''
urlpatterns = [

    path('upload/', views.SoundUploadView.as_view(), name='upload-file'),
    path('download/', views.SoundDownloadView.as_view(), name='download-file'),
    path('seed/', views.SoundSeedView.as_view(), name='sound-seed'),    
    path('guest/', views.SoundGuestView.as_view(), name='guests'),	
    path('process/', views.SoundFileCopy.as_view(), name='process'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
