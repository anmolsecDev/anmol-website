from django.shortcuts import redirect, render

# from matplotlib.pyplot import title
from blog.models import Blog

# Create your views here.


def staffView(request):
    return render(request, "blogCreate.html")


def blogView(request):
    blogs = Blog.objects.all()
    return render(request, "blogs.html", {"blogs": blogs})


def createBlog(request):
    password = request.POST["password"]
    if password == "yY3mzS^95O2c#^P":

        Blog.objects.create(
            title=request.POST["title_text"],
            body=request.POST["body_text"],
            date=request.POST["date_text"],
        )
    return redirect("/blogs/")

    # return render(
    #     request,
    #     "blogs.html",
    #     context={
    #         "title": request.POST.get("title_text", ""),
    #         "body": request.POST.get("body_text", ""),
    #     },
    # )gg
