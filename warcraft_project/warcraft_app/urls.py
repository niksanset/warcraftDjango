from django.urls import path
from warcraft_app.views import *



urlpatterns = [
   path('',MainPageView.as_view(), name='main_page'),
   path('about_game/',AboutGameView.as_view(),name='about_game'),
   path('add/', CreateContentView.as_view(),name='create_content'),
   path('image_create/',ImageCreateView.as_view(),name='image_create'),
   path('audio_create/',AudioCreateView.as_view(),name='audio_create'),
   path('video_create/',VideoCreateView.as_view(),name='video_create'),
   path('image_list/',ImageListView.as_view(),name='image_list'),
   path('video_list/',VideoListView.as_view(),name='video_list'),
   path('audio_list/',AudioListView.as_view(),name='audio_list')
  

]