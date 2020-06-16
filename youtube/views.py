from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import linkForm
from pytube import YouTube
from django.contrib import messages
from django.http import JsonResponse
import os

# Create your views here.
def home(request):
    return render(request, "home.html")


def youtube_downloder(request):
    homedir = os.path.expanduser("~")
    dirs = homedir + "/Downloads"
    if request.method == "POST":
        url = request.POST.get("text")
        print(url)
        try:
            YouTube(url).streams.first().download(homedir + "/Downloads")
            # messages.success(request, "Vedio Downloded at Download Directories")
            return JsonResponse(
                {"data": "Vedio Downloded at Download Directories"}, status=200
            )

        except:
            # messages.warning(
            #     request, "Connection Error!!! Check your network and Please Try again"
            # )
            return JsonResponse(
                {"data": "Connection Error!!! Check your network and Please Try again"},
                status=200,
            )

    return render(request, "home.html")
