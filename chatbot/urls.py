from django.urls import path
from .views import upload,home,es,unit,upload,home_faculty,youtube_search,youtube_page

urlpatterns = [
    path('upload/', upload, name='upload'),
    path('', home, name='home'),
    path('home', home_faculty, name='home_faculty'),
    path('es/', es, name='es'),
    path("unit/", unit, name='unit'),
    path('youtube_search/', youtube_search, name='youtube_search'),
    path('youtube_results/', youtube_page, name='youtube_results'),
]
