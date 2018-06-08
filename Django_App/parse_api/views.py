from django.shortcuts import render, HttpResponseRedirect, reverse, \
    HttpResponse, Http404
from .api_parse import data
from .api_parse.you_tube import *
from .api_parse.hotline_parse import *
from .FinalCourseWork.get_comments import get_description, get_comments_other
from .models import Data
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def home(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            return login_view(request)

        return render(request, "login.html", {})
    if request.method == "POST":
        name_of_product = request.POST.get('text_field')
        print(request.POST.get('text_field'))
        for element in Data.objects.all():

            if element.name.strip().lower() == request.POST.get(
                    'text_field').strip().lower():
                return render(request, "data_handle.html",
                              {"data": element.comments.split("~"),
                               "videos": eval(element.youtube),
                               "about_item": element.about,
                               "mark": element.average_mark,
                               "user_name": request.user.username,
                               "product_name": name_of_product,
                               "extra": False})
        final_comment, description, averagemark = get_description(
            name_of_product)
        videos = youtube_search(
            request.POST.get('text_field'))
        if not (final_comment and description and averagemark):
            error = "Sorry nothing with the name of {}".format(name_of_product)
            return render(request, "home.html",
                          {"error": error, "user_name": request.user.username})
            # return HttpResponseRedirect("/login")
        try:
            Data.objects.create(
                name=request.POST.get('text_field'),
                about=description,
                comments=final_comment,
                average_mark=averagemark,
                youtube=videos,
                first_video=videos[0]
            )
        except:
            pass
        return render(request, "data_handle.html",
                      {"data": final_comment.split("~"),
                       "videos": videos,
                       "about_item": description,
                       "mark": averagemark,
                       "user_name": request.user.username,
                       "product_name": name_of_product, "extra": True})
    return render(request, "home.html", {"user_name": request.user.username})


def create_post(request):
    print(request.GET["user_input"])
    comments, mark = get_comments_other(request.GET["user_input"])
    return HttpResponse(comments)


def login_view(request):
    password = request.POST.get("password")
    log = request.POST.get("login_name")
    user = authenticate(request, password=password, username=log)
    if user is not None:
        print("stufwefe")
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "login.html", {})

        # password = request.


def registrate(request):
    if request.method == "POST":
        password = request.POST.get("password")
        log = request.POST.get("login_name")
        if log and password:
            if User.objects.filter(username=log).exists():
                return render(request, "register.html",
                              {"error": "this name elready exists"})
            user = User.objects.create_user(log, log + "@mail.ru", password)
            user.save()
            return HttpResponseRedirect("/")
    return render(request, "register.html", {})


def logout_view(request):
    logout(request)
    # return render(request, "home.html", {})
    return HttpResponseRedirect("/")


def show(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            return login_view(request)
        # videos = youtube_search(request,1)
        return render(request, "login.html", {})
    data = Data.objects.all()
    videos = []
    # for element in data:
    #     videos.append(youtube_search(element, 1)[0])
    return render(request, "show.html", {"data_set": Data.objects.all(),
                                         "user_name": request.user.username})
