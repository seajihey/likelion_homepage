from django.shortcuts import render
from .models import Post


# Create your views here.
def main(request):
    return render(request, "main.html")


def introduce(request):
    return render(request, "introduce.html")


def planPage(request):
    return render(request, "planPage.html")


def projectDetail(request):
    return render(request, "projectDetail.html")


def project(request):
    return render(request, "project.html")


def mainTest(request):
    return render(request, "mainTest.html")


def activity(request):
    return render(request, "activity.html")

def introduce(request):
    return render(request, "introduce.html")


# activity record 게시글
def post_list(request):
    posts = Post.objects.all()
    return render(request, "activity.html", {"posts": posts})


def projectDetail(request):
    return render(request, "projectDetail.html")


def FAQ(request):
    return render(request, "FAQ.html")