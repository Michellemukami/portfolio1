from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include,url
from . import views

urlpatterns=[
    url('^$',views.home,name ='home'),
    url(r'^about/',views.about,name='about'),
    url(r'^project/',views.project,name='project'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)