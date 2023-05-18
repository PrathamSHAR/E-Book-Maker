from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import search

urlpatterns=[
    path('texteditor/',views.texteditor,name='Text Editor'),
    path('texteditor/upload_Book/',views.upload,name='Upload Book'),
    path('texteditor/upload_Book/addrecord/',views.addrecord,name='Add record'),
    path('bookscollection/',views.show,name='Books Collection'),
    path(r'^$', search, name='search'),
    path('submission/',views.submission,name='submission'),
    path('rate/',views.rate,name='rate'),
    path('reading/',views.reading,name='reading'),


    
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)