from django.shortcuts import render,redirect,get_object_or_404

from user.models import *
from .models import *
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return redirect('profilPage')
    return render(request,'index.html')


def filmler(request,id):
    # profil = Profile.objects.get(id = id)
    profil = get_object_or_404(Profile,id = id)
    profiller = request.user.profile_set.all()

    # Bütün filmler için
    filmler = Movie.objects.all()

    return render(request,'filmler.html',{
        'profil':profil,
        'profiller':profiller,
        'id':id,
        'filmler':filmler
    })
