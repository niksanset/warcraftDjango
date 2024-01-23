from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,DeleteView,UpdateView,CreateView
from warcraft_app.models import *
from django.urls import reverse,reverse_lazy

class MainPageView(TemplateView):
    template_name = 'warcraft_app/main.html'

class AboutGameView(TemplateView):
    template_name = 'warcraft_app/about_game.html'

class CreateContentView(TemplateView):
    template_name = 'warcraft_app/add.html'

class ImageCreateView(CreateView):
    template_name = 'warcraft_app/image_create.html'
    model = Image
    fields = ('__all__')
    success_url = reverse_lazy('image_list')
class AudioCreateView(CreateView):
    template_name = 'warcraft_app/audio_create.html'
    model = Audio
    fields = ('__all__')
class VideoCreateView(CreateView):
    template_name = 'warcraft_app/video_create.html'
    model = Video
    fields = ('__all__')


class ImageListView(ListView):
    template_name = 'warcraft_app/images_from_game.html'
    model = Image
    context_object_name = 'image_list'

class VideoListView(ListView):
    template_name = 'warcraft_app/video_from_game.html'
    model = Video
    context_object_name = 'video_list'
class AudioListView(ListView):
    template_name = 'warcraft_app/video_from_game.html'
    model = Audio
    context_object_name = 'audio_list'


