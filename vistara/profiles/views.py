from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import Profile
from vistaraapp.models import videoes

class Profileview(View):
    def get(self, request, pk, *args, **kwargs):
        profile = get_object_or_404(Profile, pk=pk)
        vid = videoes.object.all().filter(uploader=pk).order_by('-date_posted')

        context={
            'profile': profile,
            'videos': vid
        }
        return render(request, 'profiles/profile.html',context)