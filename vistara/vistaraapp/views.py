
from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from django.forms.forms import Form
from django.http import request
from django.shortcuts import render
from django.urls import reverse  
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from .models import videoes
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.list import ListView
from .forms import CommentForm
from .models import Comment
class index(ListView):
    model = videoes
    template_name='homepage.html'
    order_by= 'Date_posted'
    
class createvideo(LoginRequiredMixin, CreateView):
    model=videoes
    fields={'title','description','video_file','thumbnail'}
    template_name= 'uploadpage.html'
    def get_success_url(self):
        return reverse('Video-detail', kwargs={'pk':self.object.pk} )
    def form_valid(self, form):
        form.instance.uploader=self.request.user
        return super().form_valid(form)









class detailvid(View):
    def get(self, request, pk, *args, **kwargs):
        video = videoes.objects.get(pk=pk)

        form = CommentForm()
        comments = Comment.objects.filter(video=video).order_by('-created_on')
        context = {
            'object': video,
            'comments': comments,
            'form': form
        }
        return render(request, 'viewpage.html', context)

    def post(self, request, pk, *args, **kwargs):
        video = videoes.objects.get(pk=pk)

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                user=self.request.user,
                comment=form.cleaned_data['comment'],
                video=video
            )
            comment.save()

        comments = Comment.objects.filter(video=video).order_by('-created_on')
        context = {
            'object': video,
            'comments': comments,
            'form': form
        }
        return render(request, 'viewpage.html', context)














class updatevid(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = videoes
    fields= ['title', 'description']
    template_name= 'update.html'
    def get_success_url(self):
        return reverse('Video-detail', kwargs={'pk':self.object.pk})
    def test_func(self):
        video= self.get_object()
        return self.request.user == video.uploader

class delvid(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model=videoes
    template_name='delete.html'
    def get_success_url(self):
        return reverse('video-create')
    def test_func(self):
        video= self.get_object()
        return self.request.user == video.uploader